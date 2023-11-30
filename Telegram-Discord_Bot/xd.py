from telebot.async_telebot import AsyncTeleBot
from datetime import datetime
bot = AsyncTeleBot('6676903217:AAHEw9BM5c71WX62UsggiyWcNo-ITtblmWQ')




@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Ну привет, буду помогать\
""")



@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, "<b>{0.from_user.first_name}:</b> <i>{0.text}</i><b>; {1}</b>".format(message, datetime.fromtimestamp(message.date)), parse_mode="html")


import asyncio
asyncio.run(bot.polling())