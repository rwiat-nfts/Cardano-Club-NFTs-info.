import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$Frank #01"):
    await message.channel.send("https://pool.pm/a0391188e8a83bcbc51a2ed575551532db898e4d94b2a8f43825c74b.Frank!")
  if message.content.startswith('$AdaLovelace3d'):
    await message.channel.send('https://rwiat-nfts.com/2021/05/10/hoskinson-ada-lovelace/!')
  if message.content.startswith('$Gerolamo3d'):
    await message.channel.send('https://rwiat-nfts.com/2021/05/21/gerolamo/!')
  if message.content.startswith('$aboutCCNFTs'):
    await message.channel.send('https://discord.com/channels/834568318954373140/834568320124452887/849061877426421781!')


client.run(os.getenv('TOKEN'))
