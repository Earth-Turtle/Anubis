import random

taglines = [
    "Go give them some money.",
    "You can have a little salami, as a treat.",
    "I think you're allowed to rob a bank this time around.",
    "We've got high expectations of you now, don't mess this up.",
    "Toddbot, gift them Skyrim for the Samsung RF27T5501S Smart Fridge.",
    "However, remind yourself that overconfidence is a slow and insidious killer.",
    "You da real skibidi toilet for that",
]

stuff = {
    "city": "https://i.imgur.com/vOzYUWQ.jpeg",
    "dream": "https://i.imgur.com/la2s8Xx.jpeg",
    "ghost": "https://i.imgur.com/xr9kDQE.jpeg",
    "wind": "https://i.imgur.com/t4UWPCZ.jpeg",
    "mirror": "https://i.imgur.com/u1C6W3r.jpeg",
    "Kevin": "https://i.imgur.com/m52MVuK.jpeg",
    "pink": "https://i.imgur.com/j7xc8Sn.jpeg",
    "core": "https://i.imgur.com/W7mbDkq.jpeg",
    "wrong": "https://media.discordapp.net/attachments/1094347836382007446/1183007779997368362/20230514_131551.jpg",
}

answer = "Farewell"

# Lines for when someone tries to pin their own meme. 
# One parameter mentioning the author is expected
alerta = [
    "{} just tried to pin their own meme! Get this clown.",
    "Alerta! {} tried to pin their own meme.",
    "Your hubris shall be your downfall. {} tried to pin their own meme.",
]

def get_tagline():
    return random.choice(taglines)

def get_alerta():
    return random.choice(alerta)