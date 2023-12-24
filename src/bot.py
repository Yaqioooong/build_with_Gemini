
import os
from telegram import Update
from telegram.ext import CommandHandler,ApplicationBuilder,ContextTypes
import requestAPIs

# 构建 bot
TOKEN = os.environ['BOT_TOKEN']
proxy_url = 'http://127.0.0.1:6969/'

application = ApplicationBuilder().token(TOKEN).proxy(proxy_url).get_updates_proxy(proxy_url).build()

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

start_handler = CommandHandler('start', start)
dailywords_handler = CommandHandler('daily_words', daily_words)

application.add_handler(start_handler)
application.add_handler(dailywords_handler)
# run!
application.run_polling()

