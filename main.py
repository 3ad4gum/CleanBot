import discord
import os
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$cl'):
      await message.channel.purge(limit=100)

      await message.channel.send("Cleaned! :recycle:")
      time.sleep(2)
      await message.channel.purge(limit=1)

client.run(os.getenv('TOKEN'))