import os
import discord
import scrapper as SC
bot_token = os.environ['discord_token']

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}.format(client)")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$'):
    user_command = message.content[1:] #excludes $
    job = SC.Job(user_command)
    await message.channel.send(job.send_job_page())
    return

client.run(bot_token)