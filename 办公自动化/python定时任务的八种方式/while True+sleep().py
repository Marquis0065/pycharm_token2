# @Time: 2023/7/30 20:40
# _*_coding : utf-8 _*_
# @Authon : 
# @File : while True+sleep()
import datetime
import time
import telebot

bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")
def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%H:%M')
    return ts
def loop_monitor():
    while 1:
        print('当前时间：',time_printer())
        bot.send_message(-677235937,'第一种方法{}'.format(time_printer()))
        time.sleep(300)

if __name__ == '__main__':
    loop_monitor()
