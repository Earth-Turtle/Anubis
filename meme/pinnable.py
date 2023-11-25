from discord import Reaction, Member

from meme.lines import get_alerta, get_tagline

PIN_THRESHOLD = 3

async def check_pinnable(reaction: Reaction, user: Member):
    message = reaction.message
    if reaction.emoji == "📌":
        print("📌 reaction on post at time " + str(reaction.message.created_at) + " in channel " + reaction.message.channel.name)
        if await alerta(reaction, user):
            return
        if reaction.count >= PIN_THRESHOLD and user != message.author and not message.pinned:
            print("Users pinning post: ", [user.name async for user in reaction.users()])
            await message.pin(reason="haha funi meme")
            concur = []
            async for user in reaction.users():
                concur.append(user)
            await message.reply("Congrats! {} determined your meme should be pinned. {}".format(format_users(concur), get_tagline()))
    
async def alerta(reaction: Reaction, user: Member):
    if reaction.message.author == user:
        print(user.name + " tried to pin their own message")
        await reaction.message.reply(get_alerta().format(user.mention))
        await reaction.remove(user)
        return True
    return False

def format_users(users: list[Member]) -> str:
    if len(users) == 1: 
        return "{} has".format(users[0].mention)
    elif len(users) == 2: 
        return "{} and {} have".format(users[0].mention, users[1].mention)
    else:
        ans = ", ".join([user.mention for user in users[:-1]])
        return ans + "and {} have".format(users[-1].mention)