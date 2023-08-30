from discord import Reaction, Member

from meme.lines import get_alerta, get_tagline

async def check_pinnable(reaction: Reaction, user: Member):
    message = reaction.message
    if reaction.emoji == "📌":
        print("📌 reaction on post at time " + str(reaction.message.created_at) + " in channel " + reaction.message.channel.name)
        if await alerta(reaction, user):
            return
        if reaction.count >= 2 and user != message.author and not message.pinned:
            print("Users pinning post: ", reaction.users)
            await message.pin(reason="haha funi meme")
            concur = []
            async for user in reaction.users():
                concur.append(user)
            await message.reply("Congrats! {} and {} have determined your meme should be pinned. {}".format(*[user.mention if user != message.author else concur[-1].mention for user in concur[:2]], get_tagline()))
    
async def alerta(reaction: Reaction, user: Member):
    if reaction.message.author == user:
        print(user.name + " tried to pin their own message")
        await reaction.message.reply(get_alerta().format(user.mention))
        await reaction.remove(user)
        return True
    return False