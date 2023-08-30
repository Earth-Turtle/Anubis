import random

taglines = [
    "Go give them some money.",
    "You can have a little salami, as a treat.",
    "I think you're allowed to rob a bank this time around.",
    "We've got high expectations of you now, don't mess this up.",
    "Toddbot, gift them Skyrim for the Samsung RF27T5501S Smart Fridge.",
    "However, remind yourself that overconfidence is a slow and insidious killer.",
]

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