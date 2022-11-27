from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *



updater = Updater("5804976387:AAHkpd4hbGGAdzweWaOyZt0o7qxt1sGbmbc")

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("calcR", calcR_command))
updater.dispatcher.add_handler(CommandHandler("calcKom", calcKom_command))
print("start")
updater.start_polling()
updater.idle()