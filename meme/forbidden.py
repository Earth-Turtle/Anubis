from discord import Forbidden, Message
from datetime import timedelta
import re

YOURE_OUT = "https://media.tenor.com/BKXop7HRIdUAAAAC/out-baseball.gif"

counter = 0

async def inquisition(self, message: Message):
    
    if self.counter >= 700 and len(set(message.content.split())) >= 15:
        self.counter = 0
        await self.timeout(message)
        return

    if re.search(r"\bfried\b", message.content.lower()):
        await self.timeout(message)
    self.counter += 1
    if self.counter % 100 == 0:
        print("At {} messages on the counter".format(self.counter))

async def timeout(self, message: Message):
    try:
        await message.reply(YOURE_OUT)
        await message.author.timeout(timedelta(seconds=60))
    except Forbidden:
        await message.channel.send("Mods, send this man to the principal's office")
        await message.channel.send("Can't time them out myself")
