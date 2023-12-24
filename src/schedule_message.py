import os

from telegram import Update,Bot
from telegram.ext import CommandHandler,ApplicationBuilder,ContextTypes
import schedule
import time
import json
import requestAPIs


import requests

# 要发送消息的聊天 ID
CHAT_ID = 5001341481

# 初始化 Telegram Bot
TOKEN = os.environ['BOT_TOKEN']

def schedule_send():
    print("test method")
    text = requestAPIs.requestGemini()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url).json()
    print("send message success")

# 定时发送消息的任务
def schedule_tasks():
    print("定时任务开始执行.....")
    schedule.every().day.at("08:00").do(schedule_send)
    # schedule.every(10).seconds.do(schedule_send)
    while True:
        schedule.run_pending()
        time.sleep(1)
# 启动定时任务调度
schedule_tasks()