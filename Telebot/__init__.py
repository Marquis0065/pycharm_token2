# @Time: 2023/7/19 11:32
# _*_coding : utf-8 _*_
# @Authon : 
# @File : __init__.py
import telebot

bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "你好，马尼拉~")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()