import discord
import requests
import os

# create .env with discord bot token
my_secret = os.environ['TOKEN']

# discord client
client = discord.Client()

# terra query start
glow = 'terra1tu9yjssxslh3fd6fe908ntkquf3nd3xt8kp2u2'

query_msg = '{"state":{"contract_addr":"' + glow + '"}}'

response = requests.get(
    "https://lcd.terra.dev/wasm/contracts/" + glow + "/store",
    params={"query_msg": query_msg},
).json()

total_tickets = response['result']['total_tickets']
# terra query end

# discord code start 
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$tickets'):
    await message.channel.send('Total Tickets Locked: ' + total_tickets)

client.run(my_secret)
# discord code end
