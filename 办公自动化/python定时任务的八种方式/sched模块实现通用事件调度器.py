# @Time: 2023/7/30 21:21
# _*_coding : utf-8 _*_
# @Authon : 
# @File : sched模块实现通用事件调度器
import datetime
import time
import sched
import telebot

bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")

def time_printer():
    bot.send_message(-677235937, 'sched模块无需循环调用{}'.format(datetime.datetime.now().strftime('%H:%M')))

# 无需循环调用
def loop_monitor():
    # 生成高度器
    s = sched.scheduler(time.time,time.sleep)
    s.enter(120,1,time_printer)
    s.run()