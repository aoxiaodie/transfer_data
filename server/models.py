from django.db import models

# Create your models here.
class DBInfo(models.Model):
    id = models.AutoField(primary_key=True)
    # 数据库标识，0为源库，1为目标库
    tag = models.IntegerField()
    ip = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
