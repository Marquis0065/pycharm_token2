# @Time: 2023/7/9 11:00
# _*_coding : utf-8 _*_
# @Authon : 
# @File : __init__.py
# Update:从Telegram获取更新
from telegram import Update
#ApplicationBuilder:简单立即为构建 bot 对象
#ContextTypes:上下文类型
#CommandHandler:命令处理器
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应start命令'''
    text = '你好~我是一个bot'
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text)
start_handler = CommandHandler('start', start)
# 构建 bot
TOEKN='你 bot 的 api token'
application = ApplicationBuilder().token(TOKEN).build()
# 注册 handler
application.add_handler(start_handler)
# run!
application.run_polling()
