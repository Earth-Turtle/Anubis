from discord import Reaction, Member, User

from meme.lines import get_alerta, get_tagline
import logging

PIN_THRESHOLD = 3

async def check_pinnable(reaction: Reaction, user: Member):
    message = reaction.message
    if reaction.emoji == "📌":
        logging.info("📌 reaction on post at time " + str(reaction.message.created_at) + " in channel " + str(reaction.message.channel.__repr__()))
        if await alerta(reaction, user):
            return
        if reaction.count >= PIN_THRESHOLD and user != message.author and not message.pinned:
            concur = [user async for user in reaction.users()]
            logging.info("Users pinning post: ", [user.name for user in concur])
            await message.pin(reason="haha funi meme")
            await message.reply("Congrats! {} determined your meme should be pinned. {}".format(format_users(concur), get_tagline()))
    
async def alerta(reaction: Reaction, user: Member):
    """
    Checks if a user tried to pin their own meme. Removes the reaction and returns true if so
    
    :param reaction: The reaction performed
    :param user: the user doing the reaction
    """
    if reaction.message.author == user:
        logging.warning(user.name + " tried to pin their own message")
        await reaction.message.reply(get_alerta().format(user.mention))
        await reaction.remove(user)
        return True
    return False

def format_users(users: list[Member | User]) -> str:
    if len(users) == 1: 
        return "{} has".format(users[0].mention)
    elif len(users) == 2: 
        return "{} and {} have".format(users[0].mention, users[1].mention)
    else:
        ans = ", ".join([user.mention for user in users[:-1]])
        return ans + "and {} have".format(users[-1].mention)