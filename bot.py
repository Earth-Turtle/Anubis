# bot.py
from collections import defaultdict
import os
import logging

from discord import Intents, Message, RawReactionActionEvent, User, TextChannel, abc, Forbidden
from dotenv import load_dotenv
from discord.ext.commands import Bot, Context, CommandError

from meme.responses import find_response, check_answer, independent_response
from meme.pinnable import check_pinnable

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN: raise Exception("Set the DISCORD_TOKEN environment variable with the token for the bot")

intents = Intents.default()
intents.message_content = True
intents.moderation = True
intents.members = True

bot = Bot(command_prefix='!', intents=intents)
log_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message: Message):
    if message.author.bot: return
    await find_response(bot, message)
    await bot.process_commands(message)
    

@bot.event
async def on_raw_reaction_add(payload: RawReactionActionEvent):
    payload.member
    user = payload.member
    if user is None:
        logging.error("Reacting user doesn't exist")
        return
    channel = bot.get_channel(payload.channel_id)
    if not isinstance(channel, TextChannel):
        logging.log(logging.INFO, f"{channel} is not a guild channel, exiting reaction handling")
        return
    
    message = await channel.fetch_message(payload.message_id)
    emoji = payload.emoji
    reaction = None
    for reaction in message.reactions:
        if reaction.emoji == emoji:
            break
    if reaction is None:
        logging.error("somehow got a None reaction??")
        return
    await check_pinnable(reaction, user)
    
@bot.command(name="ping")
async def ping(ctx: Context[Bot]):
    await ctx.message.reply("pong")

@bot.command(name='reactions_given', help='Generates stats for a specific user on their reactions given')
async def reactions_given(ctx: Context[Bot], user: User, amount: int = 200, channel: TextChannel = None):
    stats: dict[str, int] = defaultdict(int)
    channel = channel if channel else ctx.channel
    async with channel.typing():
        messages = await get_history(channel, amount)
        if not messages:
            logging.warning("Message iterator was not retrieved")
            return
        
        async for message in messages:
            reactions = message.reactions
            for reaction in reactions:
                async for reactor in reaction.users():
                    if reactor.name == user.name:
                        stats[str(reaction.emoji)] += 1
                        break
    await ctx.send("Reactions given by " + user.mention)
    await ctx.send(format_stats(stats))
            
    

@bot.command(name='reactions_received', help='Genetates stats for a specific user on their reactions received. Mention the user as first argument, number of messages to check as the second')
async def reactions_received(ctx: Context[Bot], user: User, amount: int = 200, channel: TextChannel = None):
    stats: dict[str, int] = defaultdict(int)
    channel = channel if channel else ctx.channel
    await channel.typing()
    messages = await get_history(channel, amount)
    if not messages:
        logging.warning("didn't get message iterator")
        return
    count = 0
    async for message in messages:
        if message.author.name == user.name:
            count += 1
            reactions = message.reactions
            for reaction in reactions:
                stats[str(reaction.emoji)] += reaction.count
    await ctx.send(f"Reactions {user.mention} has received, from {count} posts:")
    await ctx.send(format_stats(stats))

@bot.command(name="guess", help="Make an attempt to guess the secret word")
async def check_guess(ctx: Context[Bot], guess: str):
    await check_answer(ctx, guess)

@bot.event
async def on_command_error(ctx: Context[Bot], error: CommandError):
    await ctx.send('Something went wrong, check stdout for details')
    raise error

async def get_history(channel: abc.Messageable, amount: int):
    try:
        return channel.history(limit=amount)
    except Forbidden:
        print("Bot does not have history permissions")
        await channel.send("Bot does not have history permissions")
        return None

def format_stats(stats: dict):
    if not stats:
        return "No information found for user"
    return '\n'.join([f'{k}: {v}' for k, v in sorted(stats.items(), key=lambda item: item[1], reverse=True)])


bot.run(token=TOKEN, log_handler=log_handler)