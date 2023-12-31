import os
from telegram import Update
from telegram.ext import CommandHandler,ApplicationBuilder,ContextTypes,MessageHandler,filters
import requestAPIs
import Logger
import utils
import Constants
import DBConnector as dbc

# 构建 bot
TOKEN = os.environ['BOT_TOKEN']
proxy_url = Constants.Constants.HTTP_PROXY

application = ApplicationBuilder().token(TOKEN).proxy(proxy_url).get_updates_proxy(proxy_url).build()
# 配置log格式及等级
logger = Logger.logger

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应start命令'''
    text = 'Hello, this is build_with_AI Bot, hope I can help you!'
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text)

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
    text = requestAPIs.requestGemini()
    await context.bot.send_message(chat_id=update.effective_chat.id,text=text)
    uniText = utils.unifyText(text)
    logger.warning('chat_id:' + str(update.effective_chat.id) + 'message:' + str(uniText))

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应subscribe命令'''
    id = filters_funs.split("_")[1]
    bot_name = dbc.getBotNameById(id)
    chat_id = update.effective_chat.id
    dbc.insertSunscriber(chat_id,id,bot_name)
    await context.bot.send_message(chat_id=update.effective_chat.id,text="订阅成功！")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应未知命令'''
    logger.debug('调用:unknown')
    text = "我不会这个哦~"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

filters_funs = filters.Regex('^/sub_.*')

start_handler = CommandHandler('start', start)
dailywords_handler = CommandHandler('daily_words', daily_words)
subscribe_handler = MessageHandler(filters_funs, subscribe)
unknown_handler = MessageHandler(filters.COMMAND, unknown)

application.add_handler(start_handler)
application.add_handler(dailywords_handler)
application.add_handler(unknown_handler)
application.add_handler(subscribe_handler)
# run!
application.run_polling()

