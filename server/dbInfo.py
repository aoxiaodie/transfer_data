# -*- coding: utf-8 -*-

import logging
from server import models
from django.http import JsonResponse
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def addDB(requst): # 添加数据库信息
    result = json.loads(requst.body.decode('utf-8'))
    try:
        db = models.DBInfo(tag=result["tag"], ip=result["ip"], post=result["post"], user=result["user"],
                               password=result["password"], data=result["data"])
        db.save()
        obj_db = models.DBInfo.objects.all().values()
        db_list = list(obj_db)
        return JsonResponse({"error_no": 0, "data": db_list})
    except Exception as e:
        return JsonResponse({'error_no': 1, 'error_info': str(e)})

def getDBInfo(self): # 显示数据库信息
    try:
        obj_db = models.DBInfo.objects.all().values()

        for item in obj_db:
            if item['tag'] == 0:
                item['tag'] = "是"
            elif item['tag'] == 1:
                item['tag'] = "否"

        db_lists = list(obj_db)
        return JsonResponse({"error_no": 0, "data": db_lists})
    except Exception as e:
        return JsonResponse({"error_no": 1, "data": str(e)})


def deleteDBInfo(): # 删除数据库信息
    models.DBInfo.objects.filter().delete()
