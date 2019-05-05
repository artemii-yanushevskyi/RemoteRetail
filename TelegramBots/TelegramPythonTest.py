''' To run in background on server: 
        python TelegramPython.py &
    To see what currently runs in the background:
        jobs
'''

import telebot
import time
import os
from telebot import types

from bot_token import bot_token as BOT_TOKEN

CHAT_ID = -378550435 # the PythonTelegram Group
bot = telebot.TeleBot(token=BOT_TOKEN)
current_time = time.asctime(time.localtime(time.time()))
bot.send_message(CHAT_ID, '__The bot had been started__ Current date and time\n__ _%s_' % current_time, parse_mode='Markdown')

affirmative = ['мерси', 'thanks', 'ok', '👌', '👍']
messages_bot = []

def log(message, chat_id=CHAT_ID):
    msg = bot.send_message(chat_id, message, parse_mode='Markdown', disable_notification=True)
    messages_bot.append(msg.message_id)
    return msg

timer = 300 # 300 seconds
init_timer = bot.send_message(CHAT_ID, 'Timer Init %d' % timer, parse_mode='Markdown', disable_notification=True)
while timer != 0:
    timer -= 1
    bot.edit_message_text('%d left' % timer, message_id=init_timer.message_id, chat_id=CHAT_ID)
    time.sleep(1)

@bot.message_handler(func=lambda msg: msg.text is not None and True if 'chatid' in msg.text.lower() else False)
def send_chatid(message):
    bot.send_message(message.chat.id, 'Chat ID is ```%s```' % message.chat.id, parse_mode='Markdown')

@bot.message_handler(func=lambda msg: msg.text is not None and True if 'messageid' in msg.text.lower() else False)
def send_messageid(message):
    msg = "Message ID is ```%s```" % message.message_id
    bot.send_message(message.chat.id, msg, reply_to_message_id=message.message_id, parse_mode='Markdown')   

@bot.message_handler(func=lambda msg: msg.text is not None and True if 'reaction' in msg.text.lower() else False)
def return_pool(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('a', 'v')
    markup.row('c', 'd', 'e')
    bot.send_message(message.chat.id, 'reaction:', reply_to_message_id=message.message_id, reply_markup=markup)   

@bot.message_handler()
def send_thumb(message):
    bot.reply_to(message, 'Ok 👌')

while True:
    print('Waiting for messages')
    try:
        bot.polling()
    except Exception as ex:
        time.sleep(15)
        