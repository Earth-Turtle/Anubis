from discord import *
import re
from datetime import *


class Responses:

    timeouts = {}

    def find_response(self, message: Message) -> str:
        if re.search("she [A-Za-z0-9 ]+ on my [A-Za-z0-9 ]+ till?'? (i|im|i'm|my) [A-Za-z0-9 ]+", message.content.lower()):
            return "`EXTREMELY LOUD INCORRECT BUZZER`"
        if message.author.name.lower() == "biological_jessie" and re.search(":3", message.content) and self.timer(":3", 60*60):
            return "https://cdn.discordapp.com/attachments/525173455516336129/1135766326233796608/rapidsave.com_meow-fujthvqougeb1.mp4"
        if re.search(r"\bpegging\b", message.content.lower()) and self.timer("pegging", 60*60*24):
            return "https://i.imgur.com/hAmu4dV.png"
        if re.search(r"\bfish\b", message.content) and self.timer("fish", 60*60*24):
            return "https://media.tenor.com/BiUF5Y-Q3jkAAAAC/this-man-above-me-fish-react-him-fish.gif"
        return None
    
    def timer(self, method, time):
        if method in self.timeouts:
            delta = datetime.now() - self.timeouts[method]
            if delta.total_seconds() > time:
                self.timeouts[method] = datetime.now()
                return True
            return False
        self.timeouts[method] = datetime.now()
        return True