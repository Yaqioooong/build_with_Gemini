import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(level=logging.WARNING)
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 配置控制台打印的日志
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# 配置输出到文件的日志
rotating_handler = logging.handlers.RotatingFileHandler(filename='logs/tg_chat_bot_logs.log', maxBytes=1024 * 1024 * 5, backupCount=20,encoding='utf-8')
rotating_handler.setLevel(logging.WARNING)
rotating_handler.setFormatter(formatter)
logger.addHandler(rotating_handler)
