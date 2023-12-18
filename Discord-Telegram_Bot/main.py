import discord
from datetime import datetime
import json

import asyncio
import redis
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
#@bot.command()
#async def ping(ctx):
    #await ctx.send('pong')


@bot.event
async def on_ready():
    channel = bot.get_channel(1161679620597371012)
    while True:
        message = p.get_message()
        if message and message["type"] not in ("subscribe", "unsubscribe"):
            # bot.send_message(user_id, f'{message.from_user.first_name} ({datetime.fromtimestamp(message.date)}) : {message.text}')
            await channel.send(message["data"].decode('utf-8'))
        await asyncio.sleep(0.01)


r= redis.Redis(host='redis', port=6379, db=0)
r.ping()
p=r.pubsub()
p.subscribe ("telegram-channel")

#@bot.event
#async def on_message( message):
 #   if message.author.bot:
  #      return
  #  else:
  #      await message.channel.send('{0.author}({0.created_at}): {0.content}'.format(message))
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        r.publish( 'discord-channel',  '{0.author}({0.created_at}): {0.content}'.format(message))
    # r.publish( 'discord-channel',  f('{0.author}({0.created_at}): {0.content}'.format(message))



with open("config.txt") as f:
    TOKEN = f.read().strip()

bot.run(TOKEN)
