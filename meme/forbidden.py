from discord import Message
from datetime import timedelta
import re

class Inquisitor:
    counter = 0
    YOURE_OUT = "https://media.tenor.com/BKXop7HRIdUAAAAC/out-baseball.gif"

    async def inquisition(self, message: Message):
        
        if self.counter >= 500 and len(set(message.content.split())) >= 10:
            self.counter = 0
            await self.timeout(message)
            return

        if re.search(r"\bfried\b", message.content.lower()):
            await self.timeout(message)
        self.counter += 1
        if self.counter % 100 == 0:
            print("At {} messages on the counter" % self.counter)

    async def timeout(self, message: Message):
        try:
            await message.reply(self.YOURE_OUT)
            await message.author.timeout(timedelta(seconds=60))
        except:
            await message.channel.send("Mods, send this man to the principal's office")
            await message.channel.send("Can't time them out myself")
