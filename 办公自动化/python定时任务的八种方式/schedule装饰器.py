# @Time: 2023/7/30 21:34
# _*_coding : utf-8 _*_
# @Authon : 
# @File : schedule装饰器
import time
import datetime
import telebot
from schedule import every,repeat,run_pending

bot = telebot.TeleBot("6106076754:AAHjxPSBpyjwpY-lq1iEslUufW46XQvAfr0")
@repeat(every(5).minutes)
def job():
    bot.send_message(-677235937, 'schedule装饰器{}'.format(datetime.datetime.now().strftime('%H:%M')))

while 1:
    run_pending()
    time.sleep(1)