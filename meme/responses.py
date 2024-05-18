import asyncio
from discord import Message
from discord.ext.commands import Context, Bot
import re
from datetime import datetime
from meme.lines import answer, stuff, celeste_hits


class Responses:

    timeouts = {}

    def find_response(self, bot: Bot, message: Message) -> str:
        if re.search("she [A-Za-z0-9 ]+ on my [A-Za-z0-9 ]+ (until|till?'?) (i|im|i'm|my) [A-Za-z0-9 ]+", message.content.lower()):
            return "`EXTREMELY LOUD INCORRECT BUZZER`"
        if message.author.name.lower() == "biological_jessie" and re.search(":3", message.content) and self.timer(":3", 60*60):
            return "https://cdn.discordapp.com/attachments/525173455516336129/1135766326233796608/rapidsave.com_meow-fujthvqougeb1.mp4"
        if re.search(r"\bpegging\b", message.content.lower()) and self.timer("pegging", 60*60*24):
            return "https://i.imgur.com/hAmu4dV.png"
        if re.search(r"\bfish\b", message.content) and self.timer("fish", 60*60*24):
            return "https://media.tenor.com/BiUF5Y-Q3jkAAAAC/this-man-above-me-fish-react-him-fish.gif"
        for keyword in stuff:
            pattern = r"\b" + keyword + r"\b"
            if re.search(pattern, message.content.lower()) and len(set(message.content.split())) >= 4 and not message.content.lower().startswith("|"):
                print("Keyword [{}] found in message [{}] at {}".format(keyword, message.content, message.created_at))
                # If it's in anything other than the Donta server, respond in same channel
                response_channel = message.channel
                if message.guild.id == 525147313023221775:
                    # Otherwise respond in fanatic-spiritualists
                    response_channel = bot.get_channel(1094354016286281818)
                if self.timer("keyword: {}".format(keyword), 60 * 60 * 4):
                    asyncio.run_coroutine_threadsafe(response_channel.send(stuff[keyword] + f"\n{message.author.display_name} said: `{message.content}`"), bot.loop)
        return ""
    
    def timer(self, method, time):
        if method in self.timeouts:
            delta = datetime.now() - self.timeouts[method]
            if delta.total_seconds() > time:
                self.timeouts[method] = datetime.now()
                return True
            return False
        self.timeouts[method] = datetime.now()
        return True
    
    async def check_answer(self, ctx: Context, guess: str):
        if self.timer("guess", 60 * 60 * 20):
            if guess.lower() in stuff:
                await ctx.send("No <:wyverngun:724704906954670241>\nGood try tho")
            elif guess.lower() in celeste_hits:
                await ctx.send("No <:annoyedeline:1195839611268767785>\nI sleep")
            elif guess.lower() != answer.lower():
                await ctx.send("No <:wyverngun:724704906954670241>\nI sleep")
            else:
                await ctx.send("{}, {} has done it! <@151448821254193152>, give them their prize!".format(ctx.message.guild.default_role ,ctx.author.mention))
