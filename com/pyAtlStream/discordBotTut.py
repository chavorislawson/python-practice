import discord

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print("Logged in as {0}!").format(self.user))

#     async def on_message(self, message):
#         print("Mesage from {0.author}: {0.content}".format(message))

# client = MyClient()
# client.run("clientid")#actual stuff

client = discord.Client()

@client.event
async def on_ready():
    print("Assuming direct Control as {0.user}".format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):#message can be changed to anything
        await message.channel.send("Hello!")# can do multiple awaits to do multi line

client.run("")# don't send token over internet

#go to developer portal, application you made, go to bot, click to reveal token
#that's the token you use