from discord import *
import re

class Responses:
    def find_response(self, message: Message) -> str:
        if re.search("she [A-Za-z]+ on my [A-Za-z]+ till?'? (i|im|i'm|my) [A-Za-z]+", message.content.lower()):
            return "`EXTREMELY LOUD INCORRECT BUZZER`"
        if message.author.name.lower() == "biological_jessie" and re.search(":3", message.content):
            return "https://cdn.discordapp.com/attachments/525173455516336129/1135766326233796608/rapidsave.com_meow-fujthvqougeb1.mp4"
        return None