from django.db import models

# 管理数据库
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 30)   #最长30字符的字段, 相当于varchar
    text = models.TextField()   #字符
    price = models.IntegerField()   #数字

'''
#-------------------------------数据库操作-------------------------------
# ------------------------------增
#1
    models.Article.objects.create(
        title = "e",text = "t",)
#2
    test1 = models.Article(title='runoob', text='file')
    test1.save()
# ------------------------------删
# 删除id=1的数据
#1
    test1 = models.Article.objects.get(id=1)
    test1.delete()
#2
    # models.Article.objects.filter(id=1).delete()
# 删除所有数据
    # models.Article.objects.all().delete()
# ------------------------------改
# 修改id=1的title字段, 再save, 相当于 UPDATE
#1
    test1 = models.Article.objects.get(id=1)
    test1.title = 'Google'
    test1.save()
#2
    #models.Article.objects.filter(id=1).update(title='Google')
# 修改所有的列
    # models.Article.objects.all().update(title='Google')
# ------------------------------查
# 获得所有数据, 相当于 SELECT * FROM
    list = models.Article.objects.all()        
# filter相当于 WHERE
    response2 = models.Article.objects.filter(id=1) 
# 获取单个对象
    response3 = models.Article.objects.get(id=1)     
# 限制返回的数据 相当于 OFFSET 0 LIMIT 2;
    models.Article.objects.order_by('title')[0:2]
# 数据排序
    models.Article.objects.order_by("id")
#---------------------------------------------------------------------------------------
'''