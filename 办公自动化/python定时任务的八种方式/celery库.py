# @Time: 2023/7/31 22:29
# _*_coding : utf-8 _*_
# @Authon : 
# @File : celery库
from celery import Celery
import telebot
import datetime

bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def task():
    bot.send_message(-677235937, 'celery库：{}'.format(datetime.datetime.now().strftime('%H:%M')))

app.conf.beat_schedule = {
    'task': {
        'task': 'tasks.task',
        'schedule': 60,  # 每隔10秒执行一次任务
        'args': ()
    }
}
app.conf.timezone = 'UTC'