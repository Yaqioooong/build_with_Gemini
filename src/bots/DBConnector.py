import pymysql

# 连接数据库
db = pymysql.connect(host='127.0.0.1', user='root', password='1021', db='tg_bots', charset='utf8mb4')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

def insertSunscriber(chatId: int,botId: int,botName:str):
    sql = "INSERT INTO `tg_bots`.`subscribers` (`chat_id`,`bot_id`,`bot_name`) VALUES ('chatId','botId','botName');"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

def getBotNameById(botId: int):
    sql = "SELECT `bot_name` FROM `tg_bots`.`bots` WHERE `id` = 'botId';"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()