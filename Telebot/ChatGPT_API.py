# @Time: 2023/7/20 17:44
# _*_coding : utf-8 _*_
# @Authon : 
# @File : ChatGPT_API
import openai
from telethon import TelegramClient, sync

openai.api_key = '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'

def getChat(text):
    completion = openai.Completion.create(

        engine="text-davinci-003",
        prompt=text,
        temperature=0.3,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.8,
        best_of=1,
        max_tokens=1000
    )
    return completion["choices"][0]["text"]
api_id = 29778012
api_hash = '0014bdcb9a38a91365966a9956f61e6b'
Message = "api 方法测试"
phone = '+639272771573'
# establishing a telegraph session and
# allocating it to a movable client
client = TelegramClient('chatGPT', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    # signing of the client
    client.sign_in(phone, input('Enter the code: '))

@app.on_message()

async def echo(client: client, message: Message):

    chatGpt_text = getChat(message.text)
    await message.reply(chatGpt_text)

