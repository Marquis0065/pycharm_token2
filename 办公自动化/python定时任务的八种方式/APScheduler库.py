# @Time: 2023/7/31 22:08
# _*_coding : utf-8 _*_
# @Authon : 
# @File : APScheduler库
from apscheduler.schedulers.blocking import BlockingScheduler
import telebot
import datetime

bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")

def job():
    bot.send_message(-677235937, 'APScheduler库：{}'.format(datetime.datetime.now().strftime('%H:%M')))

scheduler = BlockingScheduler()
scheduler.add_job(job,'interval',seconds=300)
scheduler.start()