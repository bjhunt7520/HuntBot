import discord
TOKEN = open("token.txt").readlines().strip()[0]
client = discord.Client()
@client.event
async def on_message(message):
    if message.channel.name == 'counting' and message.author != client.user:
        await client.send_message(message.channel, str(int(message.content)+1))
client.run(TOKEN)
