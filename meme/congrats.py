import random

taglines = [
    "Go give them some money.",
    "You can have a little salami, as a treat.",
    "I think you're allowed to rob a bank this time around.",
    "We've got high expectations of you now, don't mess this up.",
    "Toddbot, gift them Skyrim for the Samsung RF27T5501S Smart Fridge.",
    "However, remind yourself that overconfidence is a slow and insidious killer.",
]
def get_tagline():
    return random.choice(taglines)