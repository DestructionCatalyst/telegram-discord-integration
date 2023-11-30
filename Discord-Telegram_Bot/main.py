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


bot.run('MTE2MTY3NzI2MDA2NDAzOTA3Mw.GzS58m.gVbYz53-onoGGPvcG_Wmm54CNvFQfXpJ6s6Jhc')