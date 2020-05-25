# -*- coding: utf-8 -*-
import logging
from server import tableInfo
from server import dbInfo
from django.http import JsonResponse
import json
import re

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 插入表结构
def insertTable(requst):
    try:
        data = json.loads(requst.body.decode('utf-8'))
        results = data["insertTables"]

        # 格式转换
        composition = ''
        table_composition_list = {}
        table_tag = results[0]['table_name']
        num = 0
        length = len(results)
        for row in results:
            table_composition_list[table_tag] = ''
            if row['table_name'] != table_tag:
                table_composition_list[table_tag] = composition
                table_tag = row['table_name']
                composition = ''
            composition += '`' + row['column_name'] + '`' + ' ' + row['column_type']
            # composition += row['column_name'] + ' ' + row['column_type'] + ' ' + row['column_key']
            if num < length - 1:
                composition += ','
            num += 1

        table_composition_list[table_tag] = composition

        logger.info(table_composition_list)

        # 插入数据库
        if insert(table_composition_list):
            return JsonResponse({'error_no': 0, 'error_info': 'success!'})
        else:
            return JsonResponse({'error_no': 1, 'error_info': 'fail!'})
    except Exception as e:
        return JsonResponse({'error_no': 1, 'error_info': str(e)})

# 插入操作
def insert(data):
    # 连接目标库
    try:
        conn, cursor = tableInfo.connDB(1)
        # 执行建库语句
        for key, values in data.items():
            create_sql = 'CREATE TABLE IF NOT EXISTS `' + key + '` (' \
                                                                '' + values + '); '
            cursor.execute(create_sql)
            conn.commit()
            logger.info("建表语句：" + "表名：" + key + "语句：" + create_sql)
        tableInfo.closeDB(conn, cursor)
        return True
    except Exception as e:
        return  False

# 获取并插入数据
def insertData(requst):
    global create_date
    try:
        conn, cursor = tableInfo.connDB(0)
        data = json.loads(requst.body.decode('utf-8'))
        result = data['insertTables']

        table_name = {}
        column_name = ''
        i = 0
        length = len(result)
        for item in result:
            table_name[item['table_name']] = '0'
            column_name += '`' + item['column_name'] + '`'
            if i < length-1:
                column_name += ','
            i += 1

        tag = data['tag']

        for table in table_name.keys():
            sql = 'SELECT ' + column_name + ' FROM `' + table + '`;'

            logger.info(sql)
            cursor.execute(sql)
            data = cursor.fetchall()
            if tag == 1:
                data_result = tuple(dataDes(data))

            else:
                data_result = data

            create_date = []
            for row in data_result:
                velues = str(tuple(row))
                create_date.append('INSERT INTO ' + table + ' VALUES' + velues + ';')


        tableInfo.closeDB(conn, cursor)

        if insertDatas(create_date):
            dbInfo.deleteDBInfo()
            return JsonResponse({'error_no': 0, 'error_info': 'success!'})

        return JsonResponse({'error_no': 0, 'error_info': 'fail!'})

    except Exception as e:
        return JsonResponse({'error_no': 1, 'error_info': str(e)})

def insertDatas(sql):
    try:
        conn, cursor = tableInfo.connDB(1)
        for row in sql:
            cursor.execute(row)
            conn.commit()
        tableInfo.closeDB(conn, cursor)
        return True
    except Exception as e:
        return False

# 脱敏
def dataDes(results):
    date_list_in = []
    data_list_out = []
    for row in results:
        for item in row:
            if isinstance(item, str):
                if re.match(r"^1[35678]\d{9}$", item):
                    new_item = item[0:3] + '****' + item[7:11]
                    date_list_in.append(new_item)
                if re.match(
                        r"^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$",
                        item) or re.match(
                        r"^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}[0-9Xx]$", item):
                    new_item = item[0:2] + '****' + item[6:14] + '****'
                    date_list_in.append(new_item)
                else:
                    date_list_in.append(item)
            else:
                date_list_in.append(item)
        data_list_out.append(date_list_in)
        date_list_in = []
    return data_list_out

