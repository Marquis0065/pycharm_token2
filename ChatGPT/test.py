# @Time: 2023/7/24 17:44
# _*_coding : utf-8 _*_
# @Authon : 
# @File : test
import telebot
from telegram.ext import Updater, MessageHandler,filters
import openai
bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")
# 设置OpenAI API密钥
openai.api_key ="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"
# TELEGRAM_BOT_TOKEN="6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y"
# 处理用户消息
@bot.message_handler(content_types='text')
def handle_message(message):

    # 使用ChatGPT生成回复
    response = openai.Completion.create(
        engine='davinci',
        prompt=message.text,
        max_tokens=50,
        temperature=0.7
       )
    reply = response.choices[0].text.strip()
    # 发送回复消息给用户
    bot.send_message(chat_id=6210512460, text=reply)

bot.infinity_polling()