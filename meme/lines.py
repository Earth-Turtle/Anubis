import random

taglines = [
    "Go give them some money.",
    "You can have a little salami, as a treat.",
    "I think you're allowed to rob a bank this time around.",
    "We've got high expectations of you now, don't mess this up.",
    "Toddbot, gift them Skyrim for the Samsung RF27T5501S Smart Fridge.",
    "However, remind yourself that overconfidence is a slow and insidious killer.",
    "You da real skibidi toilet for that.",
    "Chat thinks it's funny too."
]

stuff = {
    # "city": "https://i.imgur.com/vOzYUWQ.jpeg",
    "granny": "https://i.imgur.com/vOzYUWQ.jpeg",

    # "dream": "https://i.imgur.com/la2s8Xx.jpeg",
    "reflection": "https://i.imgur.com/la2s8Xx.jpeg",
    "twin": "https://i.imgur.com/la2s8Xx.jpeg",

    "ghost": "https://i.imgur.com/xr9kDQE.jpeg",
    "hotel": "https://i.imgur.com/xr9kDQE.jpeg",
    "clean": "https://i.imgur.com/xr9kDQE.jpeg",

    # "wind": "https://i.imgur.com/t4UWPCZ.jpeg",
    # "windy": "https://i.imgur.com/t4UWPCZ.jpeg",
    "cloud": "https://i.imgur.com/t4UWPCZ.jpeg",

    "mirror": "https://i.imgur.com/u1C6W3r.jpeg",
    "mirrored": "https://i.imgur.com/u1C6W3r.jpeg",

    "feather": "https://i.imgur.com/m52MVuK.jpeg",
    "kevin": "https://i.imgur.com/m52MVuK.jpeg",
    "bumper": "https://i.imgur.com/m52MVuK.jpeg",

    # "pink": "https://i.imgur.com/j7xc8Sn.jpeg",
    "peak": "https://i.imgur.com/j7xc8Sn.jpeg",
    "flag": "https://i.imgur.com/j7xc8Sn.jpeg",

    # "core": "https://i.imgur.com/W7mbDkq.jpeg",
    "hot": "https://i.imgur.com/W7mbDkq.jpeg",
    "cold": "https://i.imgur.com/W7mbDkq.jpeg",
    "switch": "https://i.imgur.com/W7mbDkq.jpeg",

    "perfect": "https://avatars.cloudflare.steamstatic.com/257da88900d59c704efae09a6731252af2034719_full.jpg"
}

celeste_hits = [
    "celeste",
    "mountain",
    "madeline",
    "badeline",
    "heart",
    "crow",
    "theo",
    "dash",
    "trans",
    "strawberry",
    "granny",
    "cassette",
    "reina",
]

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