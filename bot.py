# bot.py
import asyncio
from collections import defaultdict
import os

from discord import *
from dotenv import load_dotenv
from discord.ext.commands import Bot, Context

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True


bot = Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='reactions_given', help='Generates stats for a specific user on their reactions given')
async def reactions_given(ctx: Context, user: User, amount: int = 200):
    stats = defaultdict(int)
    messages = asyncio.run(get_history(ctx.channel, amount))
    for message in messages:
        reactions = message.reactions
        for reaction in reactions:
            async for reactor in reaction.users():
                if reactor.name == user.name:
                    stats[str(reaction.emoji)] += 1
    output = '\n'.join([f'{k}: {v}' for k, v in sorted(stats.items(), key=lambda item: item[1], reverse=True)])
    await ctx.send("Stats for " + user.mention)
    await ctx.send(output)
            
    

@bot.command(name='reactions_received', help='Genetates stats for a specific user on their reactions received')
async def reactions_received(ctx: Context, user: User, amount: int = 200):
    pass

@bot.event
async def on_command_error(ctx, error):
    await ctx.send('Something went wrong, check stdout for details')
    raise error

async def get_history(channel: abc.Messageable, amount: int) -> list[Message]:
    try:
        async with channel.typing():
            await asyncio.sleep(5)
        return [m async for m in channel.history(limit=amount)]
    except Forbidden:
        print("Bot does not have history permissions")
        await channel.send("Bot does not have history permissions")
        return None

        


bot.run(TOKEN)