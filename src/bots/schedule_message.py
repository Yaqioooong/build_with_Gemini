import os
import schedule
import time
import requestAPIs
import requests
import Logger
import utils
import Constants

# 要发送消息的聊天 ID
CHAT_ID = 5001341481

# 初始化 Telegram Bot
TOKEN = os.environ['BOT_TOKEN']
# 配置log格式及等级
logger = Logger.logger
def schedule_send():
    print("test method")
    text = requestAPIs.requestGemini()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url).json()
    uniText = utils.unifyText(text)
    logger.warning('定时任务执行:chat_id:' + str(CHAT_ID) + 'message:' + str(uniText))
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