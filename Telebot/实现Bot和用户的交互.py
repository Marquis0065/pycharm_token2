# @Time: 2023/7/24 15:30
# _*_coding : utf-8 _*_
# @Authon : 
# @File : 实现Bot和用户的交互
import telebot
bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "你好，马尼拉~")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

# 只处理用户发送内容为“文件”和“音频”的message
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
	bot.reply_to(message,'谢谢你发送的文件和音频，已经收到了')


# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass

# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	pass

# Handles all messages for which the lambda returns True
@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	pass

# Which could also be defined as:
def test_message(message):
	return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
	pass

# Handlers can be stacked to create a function which will be called if either message_handler is eligible
# This handler will be called if the message starts with '/hello' OR is some emoji
@bot.message_handler(commands=['hello'])
# @bot.message_handler(func=lambda msg: msg.text.encode("utf-8") == SOME_FANCY_EMOJI)
def send_something(message):
    pass

bot.infinity_polling()




# 官方给出的filters支持的类型如下：
#
# name	argument	Condition
# content_types	list of strings (default [’text’])	True if message.content_type is in the list of strings.
# regexp	a regular expression as a string	True if re.search(regexp_arg) returns True and message.content_type == ’text’ (See https://docs.python.org/2/library/re.html)
# commands	list of strings	True if message.content_type == ’text’ and message.text starts with a command that is in the list of strings.
# chat_types	list of chat types	True if message.chat.type in your filter
# func	a function (lambda or function reference)	True if the lambda or function reference returns True