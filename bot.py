# bot.py
from collections import defaultdict
import os
import logging

from discord import Intents, Interaction, Message, RawReactionActionEvent, User, TextChannel, abc, Forbidden, app_commands
from discord.abc import MessageableChannel
from dotenv import load_dotenv
from discord.ext.commands import Bot, Context, CommandError # pyright: ignore[reportMissingTypeStubs]

from meme.responses import find_response
from meme.pinnable import check_pinnable

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN: raise Exception("Set the DISCORD_TOKEN environment variable with the token for the bot")

intents = Intents.default()
intents.message_content = True
intents.moderation = True
intents.members = True

bot = Bot(command_prefix='!', intents=intents)
command_tree = app_commands.CommandTree(bot)
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
    
@command_tree.command(name="ping")
async def ping(interaction: Interaction):
    if not isinstance(interaction.channel, TextChannel):
        logging.warning("Interaction attempted in non-Text channel", interaction)
        return
    await interaction.channel.send("pong")

@command_tree.command(name="Reactions given", description="Information on the reactions your or a specific user have given")
async def reactions_given_command(interaction: Interaction, user: User | None, amount: int = 200, channel: MessageableChannel | None = None):
    """
    :param interaction: Context for the command invocation
    :param user: The user to analyze. If not provided, will use the user invoking the command
    :param amount: How many messages to analyze
    :param channel: The channel to search for messages. If not provided, will use the channel the command is used in
    """
    if not isinstance(interaction.channel, MessageableChannel):
        logging.warning("Can't interact with channel provided in interaction", interaction)
        return
    if channel:
        channel_to_analyze = channel
    else:
        channel_to_analyze = interaction.channel
    stats: dict[str, int] = defaultdict(int)
    user_to_analyze = user if user else interaction.user

    async with interaction.channel.typing():
        async for message in channel_to_analyze.history(limit=amount):
            for reaction in message.reactions:
                async for reactor in reaction.users():
                    if reactor.name == user_to_analyze.name:
                        stats[str(reaction.emoji)] += 1
                        break
    # TODO: clean up these messages, check format_stats for example-ish
    await interaction.channel.send("Reactions given by:")
    await interaction.channel.send(str(stats))

@command_tree.command(name="Reactions received", description="Information on the reactions you have received")
async def reactions_received_command(interaction: Interaction, user: User | None = None, amount: int = 200, channel: MessageableChannel | None = None):
    """
    :param interaction: Context for the command invocation
    :param user: The user to analyze. If not provided, will use the user invoking the command
    :param amount: How many messages to analyze
    :param channel: The channel to search for messages. If not provided, will use the channel the command is used in
    """
    if not isinstance(interaction.channel, MessageableChannel):
        logging.warning("Can't analyze messages in this channel", interaction)
        return
    stats: dict[str, int] = defaultdict(int)
    user_to_analyze = user if user else interaction.user
    channel_to_analyze = channel if channel else interaction.channel
    posts_from_user = 0
    async with interaction.channel.typing():
        async for message in channel_to_analyze.history(limit=amount):
            if message.author.name == user_to_analyze.name:
                posts_from_user += 1
                for reaction in message.reactions:
                    stats[str(reaction.emoji)] += reaction.count
    # TODO: make pretty
    await interaction.channel.send(f"Reactions {user_to_analyze.mention} has received")
    await interaction.channel.send(str(stats))

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

def format_stats(stats: dict[str, int]):
    if not stats:
        return "No information found for user"
    return '\n'.join([f'{k}: {v}' for k, v in sorted(stats.items(), key=lambda item: item[1], reverse=True)])


bot.run(token=TOKEN, log_handler=log_handler)