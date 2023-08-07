# bot.py
from collections import defaultdict
import os

from discord import *
from dotenv import load_dotenv
from discord.ext.commands import Bot, Context

from meme.responses import Responses
from meme.congrats import get_tagline

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True
intents.moderation = True

bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message: Message):
    responder = Responses()
    response = responder.find_response(message)
    if response:
        await message.reply(response)

@bot.event
async def on_reaction_add(reaction: Reaction, user: Member):
    message = reaction.message
    if reaction.emoji == "📌" and reaction.count >= 2 and user != message.author and not message.pinned:
        print("entered bloc")
        await message.pin(reason="haha funi meme")
        concur = []
        async for user in reaction.users():
            concur.append(user)
        await message.reply("Congrats! {} and {} have determined your meme should be pinned. {}".format(*[user.mention if user != message.author else concur[-1].mention for user in concur[:2]], get_tagline()))

@bot.command(name='reactions_given', help='Generates stats for a specific user on their reactions given')
async def reactions_given(ctx: Context, user: User, amount: int = 200, channel: TextChannel = None):
    stats = defaultdict(int)
    channel = channel if channel else ctx.channel
    await channel.typing()
    messages = await get_history(channel, amount)
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
async def reactions_received(ctx: Context, user: User, amount: int = 200, channel: TextChannel = None):
    stats = defaultdict(int)
    channel = channel if channel else ctx.channel
    await channel.typing()
    messages = await get_history(channel, amount)
    count = 0
    async for message in messages:
        if message.author.name == user.name:
            count += 1
            reactions = message.reactions
            for reaction in reactions:
                stats[str(reaction.emoji)] += reaction.count
    await ctx.send(f"Reactions {user.mention} has received, from {count} posts:")
    await ctx.send(format_stats(stats))

@bot.event
async def on_command_error(ctx, error):
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


bot.run(TOKEN)