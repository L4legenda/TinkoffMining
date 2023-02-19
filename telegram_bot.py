import telebot

from config import TELEGRAM_TOKEN, ID_ACCOUNT_TELEGRAM

bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')

def send_message(text):
    print("== MESSAGE ==")
    print(text)
    bot.send_message(ID_ACCOUNT_TELEGRAM, text)