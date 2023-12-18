from typing import Final
import telebot
from datetime import datetime
import redis
import time
import asyncio
from telebot.async_telebot import AsyncTeleBot

TOKEN = None
with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = AsyncTeleBot(TOKEN)
BOT_USERNAME: Final = '@Teldispp'
ch_id = -1001522399768

r = redis.Redis(host='redis', port=6379, db=0)
r.ping()
p = r.pubsub()
p.subscribe("discord-channel")

# responses
@bot.message_handler(commands=["start"])
async def start(message):
    ch_id = message.chat.id
    await bot.send_message(message.chat.id, 'Доброе утро! Cпасибо, что разбудили.')

@bot.message_handler(commands=["help"])
async def help(message):
    await bot.send_message(message.chat.id, 'Я здесь, чтобы помочь синхронизировать сообщения с двух чатов.(пока только повторяю)')

@bot.message_handler(func=lambda message: True)
async def receive_message(message):
    print("we got here")
    await r.publish('telegram-channel', f'{message.from_user.first_name} ({datetime.fromtimestamp(message.date)}) : {message.text}')



async def loop():
    while True:
        message = p.get_message()
        if message and message["type"] not in ("subscribe", "unsubscribe"):
            await bot.send_message(ch_id, message["data"].decode('utf-8'))
        await asyncio.sleep(0.01)

async def main():
    await asyncio.gather(loop(), bot.polling())
asyncio.run(main())

