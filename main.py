import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv
import utils

def my_excepthook(type, value, tb):
    # you can log the exception to a file here
    print('In My Exception Handler')

    # the following line does the default (prints it to err)
    sys.__excepthook__(type, value, tb)

sys.excepthook = my_excepthook

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

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

    if update.callback_query:
        print("ok")
        bot.answer_callback_query(update.callback_query.id)

    button_list = [
        InlineKeyboardButton("«", callback_data="1"),
        InlineKeyboardButton("»", callback_data="2")
    ]

    
    reply_markup = InlineKeyboardMarkup(utils.build_menu(button_list, n_cols=2))

    bot.send_message(chat_id=update.message.chat_id, 
                     text=answer, 
                     parse_mode=ParseMode.MARKDOWN,
                     reply_markup=reply_markup)

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