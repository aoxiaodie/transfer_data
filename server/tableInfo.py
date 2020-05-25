# -*- coding: utf-8 -*-
import pymysql
import logging
from django.http import JsonResponse
from server import models
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 获取数据库连接信息
def getSourceConnInfo(tag):
    obj_db = models.DBInfo.objects.get(tag=tag)
    return obj_db

# 连接数据库
def connDB(tag):
    db = getSourceConnInfo(tag)
    host = db.ip
    port = int(db.post)
    user = db.user
    password = db.password
    data = db.data
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=data, charset='utf8')
    cursor = conn.cursor()
    return conn, cursor

# 关闭连接
def closeDB(conn, cursor):
    conn.close()
    cursor.close()

# 查询并获取源表结构
def getTableInfo(requst):
    try:
        data = json.loads(requst.body.decode('utf-8'))
        table_name = data["table_name"]

        conn, cursor = connDB(0)
        sql = (
            f"SELECT TABLE_NAME ,COLUMN_NAME ,COLUMN_TYPE, COLUMN_KEY FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME LIKE '%{table_name}%'")
        cursor.execute(sql)
        table_all = cursor.fetchall()

        closeDB(conn, cursor)

        table_dict = []
        keys = ("table_name", "column_name", "column_type", "column_key")
        for item in table_all:
            table_dict.append({k: v for k, v in zip(keys, item)})

        logger.info(table_dict)
        return JsonResponse({'error_no': 0, 'data': list(table_dict)})

    except Exception as e:
        return JsonResponse({'error_no': 1, 'error_info': str(e)})
