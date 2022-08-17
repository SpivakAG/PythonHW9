from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler,Filters
from scripts import *
from tic import game

updater = Updater('5468072039:AAGHQSdcTnrnu2lJU9YDbKAeKWI12IZaw1o')

updater.dispatcher.add_handler(CommandHandler('game', game))
#updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))

print('server start')
updater.start_polling()
updater.idle()