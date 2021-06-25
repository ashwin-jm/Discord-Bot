import discord
import random

TOKEN = 'ODUyOTg1OTY1OTkxMDM0OTAw.YMOzFg.mTxD2WQtIZWcsXj85U8SuLC1vqw'

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('Hello'):
        await message.channel.send("Hey !! How are you feeling today - happy or sad ?")

    if message.content == 'Happy':
        await message.channel.send("Glad to know that !!")

    if message.content == 'Sad':
        await message.channel.send("Don't be sad. Nothing is permanent. Your sadness will also go !!")

    if message.content == 'Thank you':
        await message.channel.send("You're welcome")

    if message.content.startswith('Bye'):
        await message.channel.send("Tataa")    

@client.event
async def on_ready():
    general_channel = client.get_channel(852979713239679061)
    await general_channel.send('I am online')
    
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send("Welcome  {memmber}")


client.run(TOKEN)