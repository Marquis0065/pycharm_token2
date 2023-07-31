import telegram
from telegram.ext import Updater, MessageHandler,filters, CommandHandler
import openai

# 设置OpenAI API密钥
openai.api_key="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"
TELEGRAM_BOT_TOKEN="6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y"
# 处理用户消息
def handle_message(update, context):
    message = update.message.text
    # 使用ChatGPT生成回复
    response = openai.Completion.create(
        engine='davinci',
        prompt=message,
        max_tokens=50,
        temperature=0.7
       )
    reply = response.choices[0].text.strip()
    # 发送回复消息给用户
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

def main():
    # 创建Telegram机器人实例
    # updater = Updater(telegram.Bot(TELEGRAM_BOT_TOKEN), use_context=True)
    # dispatcher = updater.dispatcher()
    updater = Updater(telegram.Bot(TELEGRAM_BOT_TOKEN))
    message_handler = MessageHandler(filters.text, handle_message)
    updater.dispatcher.add_handler(message_handler)
    # 添加消息处理程序
    # message_handler = MessageHandler(filters.text, handle_message)
    # dispatcher.add_handler(message_handler)
    # 启动机器人
    updater.start_polling
    updater.idle()

if __name__=='__main__':
    main()