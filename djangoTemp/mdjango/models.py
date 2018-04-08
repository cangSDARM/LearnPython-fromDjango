from django.db import models

# 管理数据库
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 30)   #最长30字符的字段, 相当于varchar
    text = models.TextField()   #字符
