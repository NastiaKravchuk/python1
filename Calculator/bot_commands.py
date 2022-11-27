from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
import calc_for_bot as cb


def hi_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'hi {update.effective_user.first_name}')
    log(update, context)
def time_command(update: Update, context: CallbackContext):
    update.message.reply_text(f' {datetime.datetime.now().time()}')
    log(update, context)
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/time\n/culk\n/culkKom\n/help')
    log(update, context)
def calcR_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    num1 = items[1]
    oper = items[2]
    num2 = items[3]
    result = cb.calc_botR(num1,oper, num2)
    print(result)
    update.message.reply_text(f'{num1} {oper} {num2} = {result}')
    log(update, context)
def calcKom_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    num1 = items[1]
    num2 = items[2]
    oper = items[3]
    number1 = items[4]
    number2 = items[5]
    result = cb.calc_botK(num1,num2, oper, number1, number2)
    print(result)
    update.message.reply_text(f'({num1}+ {num2}i) {oper} ({number1}+{number2}i) = {result}')
    log(update, context)
   