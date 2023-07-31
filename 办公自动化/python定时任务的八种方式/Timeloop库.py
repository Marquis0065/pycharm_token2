# @Time: 2023/7/30 20:50
# _*_coding : utf-8 _*_
# @Authon : 
# @File : Timeloop库
from timeloop import Timeloop
import time
import datetime
from datetime import timedelta
import telebot

# bot = telebot.TeleBot('6106076754:AAHjxPSBpyjwpY-lq1iEslUufW46XQvAfr0')
bot_m = telebot.TeleBot('6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y')
t1 = Timeloop()

@t1.job(interval=timedelta(seconds=30))
def loop_monitor():
    bot_m.send_message(-677235937,'Timeloop库运行定时任务：{}'.format(datetime.datetime.now().strftime('%H:%M')))

