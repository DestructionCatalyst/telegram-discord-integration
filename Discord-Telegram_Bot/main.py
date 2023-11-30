import discord
from datetime import datetime
import json
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message( message):
    if message.author.bot:
        return
    else:
        await message.channel.send('{0.author}({0.created_at}): {0.content}'.format(message))

with open("config.txt") as f:
    TOKEN = f.read().strip()

bot.run(TOKEN)