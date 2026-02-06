from datetime import timedelta
from typing import Awaitable, Callable
from discord import Message
from discord.ext.commands import Bot # pyright: ignore[reportMissingTypeStubs]
import re
from tools import timer

async def she_x_on_my_y(message: Message) -> bool:
    if re.search("she .+ on my .+ (until|till?'?) (i|im|i'm|my) .+", message.content.lower()):
        await message.reply("`EXTREMELY LOUD INCORRECT BUZZER`")
        return True
    return False

async def jess_colon_three(message: Message) -> bool:
    if message.author.name.lower() == "biological_jessie" and re.search(r"\b:3\b", message.content) and timer(":3", timedelta(hours=1)):
        await message.reply("https://cdn.discordapp.com/attachments/525173455516336129/1135766326233796608/rapidsave.com_meow-fujthvqougeb1.mp4")
        return True
    return False
    
async def pegging(message: Message) -> bool:
    if re.search(r"\bpegging\b", message.content.lower()) and timer("pegging", timedelta(hours=4)):
        await message.reply("https://i.imgur.com/hAmu4dV.png")
        return True
    return False

async def fish(message: Message) -> bool:
    if re.search(r"\bfish\b", message.content) and timer("fish", timedelta(days=3)):
        await message.reply("https://media.tenor.com/BiUF5Y-Q3jkAAAAC/this-man-above-me-fish-react-him-fish.gif")
        return True
    return False

async def luther(message: Message) -> bool:
    match = re.search(r"r\w?e\w?f\w?o\w?r\w?m\w?", message.content, re.IGNORECASE)
    if match and match.group(0) != "reform" and timer("reform", timedelta(days=6)):
        found = match.group(0)
        await message.reply("`{}`\n".format(found))
        return True
    return False

checks: list[Callable[[Message], Awaitable[bool]]] = [
    she_x_on_my_y,
    jess_colon_three,
    pegging,
    fish,
    luther
]

async def find_response(bot: Bot, message: Message) -> None:
    for check in checks:
        if await check(message):
            break
