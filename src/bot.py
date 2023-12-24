
import os
from telegram import Update
from telegram.ext import CommandHandler,ApplicationBuilder,ContextTypes
import json
import requests

# 构建 bot
TOKEN = os.environ['BOT_TOKEN']
proxy_url = 'http://127.0.0.1:6969/'

application = ApplicationBuilder().token(TOKEN).proxy(proxy_url).get_updates_proxy(proxy_url).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应start命令'''
    text = '你好~我是一个bot'
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text)

def requestGemini():
    proxies = {
        'http': 'http://127.0.0.1:6969',
        'https': 'https://127.0.0.1:6969',
    }
    headers = {
        'Content-Type': 'application/json',
    }
    params = {
        # 此处填写GEMINI API KEY
        'key': os.environ['KEY_GEMINI']
    }
    json_data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': 'generate a random word in Chinese ans English respectively',
                    },
                ],
            },
        ],
    }
    response = requests.post(
        'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent',
        params=params,
        headers=headers,
        json=json_data,
        proxies=proxies
    )
    jsonStr = response.text
    jsonData = json.loads(jsonStr)
    res = jsonData['candidates'][0]['content']['parts'][0]['text']
    return res

def escape_special_chars(str1):
    """
    将字符串中的特殊字符加上转义符

    Args:
        str1: 待处理的字符串

    Returns:
        转义后的字符串
    """

    return str1.replace('\\', r'\\').replace('"', r'\"').replace("'", r"\'").replace('{', r'\{').replace('}', r'\}').replace('[', r'\[').replace(']', r'\]').replace('(', r'\(').replace(')', r'\)')

async def daily_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应dailywords命令'''
    text = requestGemini()
    # res = escape_special_chars(text)
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text)

start_handler = CommandHandler('start', start)
dailywords_handler = CommandHandler('daily_words', daily_words)

application.add_handler(start_handler)
application.add_handler(dailywords_handler)
# run!
application.run_polling()

