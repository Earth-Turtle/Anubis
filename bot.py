# bot.py
import os

from discord import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = Client(intents=Intents(value=275952031808))

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)