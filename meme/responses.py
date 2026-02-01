from datetime import timedelta
from discord import Message
from discord.ext.commands import Bot # pyright: ignore[reportMissingTypeStubs]
import re
from tools import timer

async def find_response(bot: Bot, message: Message) -> None:
    await she_x_on_my_y(message)
    await jess_colon_three(message)
    await pegging(message)
    await fish(message)

    
async def she_x_on_my_y(message: Message):
    if re.search("she .+ on my .+ (until|till?'?) (i|im|i'm|my) .+", message.content.lower()):
        await message.reply("`EXTREMELY LOUD INCORRECT BUZZER`")

async def jess_colon_three(message: Message):
    if message.author.name.lower() == "biological_jessie" and re.search(r"\b:3\b", message.content) and timer(":3", timedelta(hours=1)):
        await message.reply("https://cdn.discordapp.com/attachments/525173455516336129/1135766326233796608/rapidsave.com_meow-fujthvqougeb1.mp4")
    
async def pegging(message: Message):
    if re.search(r"\bpegging\b", message.content.lower()) and timer("pegging", timedelta(hours=4)):
        await message.reply("https://i.imgur.com/hAmu4dV.png")

async def fish(message: Message):
    if re.search(r"\bfish\b", message.content) and timer("fish", timedelta(days=3)):
        await message.reply("https://media.tenor.com/BiUF5Y-Q3jkAAAAC/this-man-above-me-fish-react-him-fish.gif")
