import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        print('client user: ', client.user)
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run('NjkxMTE1MzgxNTkwNDU4Mzkx.XnbTjg.8_1A6sGliVvKUWWqGYrBqqGYPak')

