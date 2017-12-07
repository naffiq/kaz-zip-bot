import os
from os.path import join, dirname
from dotenv import load_dotenv
import utils

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

updater = Updater(token = os.environ.get("BOT_TOKEN"))

dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id, 
        text = """Привет!
Напиши мне свой адрес и я скажу тебе твой почтовый индекс.
Например: Алматы, Байзакова 298."""
    )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def address(bot, update):
    address_text = update.message.text
    answer = "*Адрес:* %s\n*Почтовый индекс:* %s\n*Старый почтовый индекс:* %s" % utils.get_zip_code(address_text)
    
    bot.send_message(chat_id=update.message.chat_id, 
                     text=answer, 
                     parse_mode=ParseMode.MARKDOWN)

address_handler = MessageHandler(Filters.text, address)
dispatcher.add_handler(address_handler)

def about(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="""
Я был создан @naffiq в свободное от работы время. Мои исходники можно посмотреть тут: 
https://github.com/naffiq/kaz-zip-bot
""")

start_handler = CommandHandler('about', about)
dispatcher.add_handler(start_handler)

updater.start_polling()