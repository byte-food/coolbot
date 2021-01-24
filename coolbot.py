import discord
import random

TOKEN = "ODAyNzg5NDM3ODE3MjI1MjM2.YA0V7Q.fHeeRjarnzMeiIkeGac9vdpcBXc"
GUILD = "ooga booga"

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Heil {member.name}, abook a9la3'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    members = message.guild.members
    memberlist = []
    for member in message.guild.members:
        memberlist.append(member.name)
    memberlist.remove("H0tMess007")
    if message.content == "who's cool?":
        response = random.choice(memberlist)
        await message.channel.send(response+" is the cool person of the day!")

client.run(TOKEN)