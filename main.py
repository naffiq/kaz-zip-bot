import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

updater = Updater(token = os.environ.get("BOT_TOKEN"))

dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет! Напиши мне свой адрес и я скажу тебе твой почтовый индекс.\nНапример: Алматы, Байзакова 298")

def get_zip_code(address):
    r = requests.get("https://api.post.kz/api/byAddress/%s?from=0" % address)
    rJson = r.json()

    code = rJson['data'][0]['postcode']
    address_rus = rJson['data'][0]['addressRus']
    return (address_rus, code)

def address(bot, update):
    address_text = update.message.text
    answer = "Адрес: %s\nПочтовый индекс: %s" % get_zip_code(address_text)

    print("Question:\n%s\nAnswer:\n%s\n" % (address_text, answer))
    
    bot.send_message(chat_id=update.message.chat_id, text=answer)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

address_handler = MessageHandler(Filters.text, address)
dispatcher.add_handler(address_handler)

updater.start_polling()