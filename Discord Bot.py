# Work with Python 3.6
import discord

client = discord.Client()

    
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    print("The message's content was", message.content)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run("NDkzNTU2Njk5MTE5MjIyNzkz.Dosgcg.VDZQ5OWU9qlGntI5Mn3F4ydiT3o")
