from typing import Final
import telebot
from datetime import datetime

TOKEN = None
with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)
BOT_USERNAME: Final = '@Teldispp'


# responses
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Доброе утро! Cпасибо, что разбудили.')

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, 'Я здесь, чтобы помочь синхронизировать сообщения с двух чатов.(пока только повторяю)')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name} ({datetime.fromtimestamp(message.date)}) : {message.text}')

@bot.message_handler(content_types=['text', 'video'])
def echo_video(message):
    if message.caption == None:
        bot.send_video(message.chat.id, message.video.file_id, caption = f'{message.from_user.first_name} ({datetime.fromtimestamp(message.date)}) : No text was in message')
    else:
        bot.send_video(message.chat.id, message.video.file_id, caption = f'{message.from_user.first_name} ({datetime.fromtimestamp(message.date)}) : {message.caption}')

@bot.message_handler(content_types=['text', 'photo'])
def echo_photo(message):
    if message.caption == None:
        bot.send_photo(message.chat.id, message.photo[0].file_id, caption = f'{message.from_user.first_name} ({datetime.fromtimestamp(message.date)}) : No text was in message')
    else:
        bot.send_photo(message.chat.id, message.photo[0].file_id, f'{message.from_user.first_name} ({datetime.fromtimestamp(message.date)}) : {message.caption}')


bot.polling()
print("Polling...")

