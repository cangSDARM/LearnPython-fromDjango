from django.db import models

# 管理数据库
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 30)   #最长30字符的字段, 相当于varchar, 参数与sql相似, 具体查看__init__方法
    text = models.TextField()   #字符
    price = models.IntegerField()   #数字
    authors = models.ManyToManyField("Author") #多对多: 放在哪个表都行. 只能通过对象绑定(通过创建第三张表分别一对多模拟出来的)
    publiser = models.ForeignKey("Publiser", to_field="nid")  #一对多: 谁是多, 外键在哪. to_filed: 指定外键, 必须是唯一
    oneother = models.OneToOneField("elses")  #一对一: (联合唯一的一对多)

'''
#--------------------------数据库操作-ORM：Object Relational Mapping(关系对象映射)-----------------------
#数据库查询objects返回一个QuerySet对象
#可迭代,可切片,惰性计算(查询优化)
# books=models.Book.objects.all()[:10]  #切片
# models.Publish.objects.all().iterator() #迭代
# ------------------------------增
#1
    models.Article.objects.create(
        title = "e",text = "t",)
#2
    test1 = models.Article.objects.create(**{"title":'runoob', "text":'file'})
#3
    tes1 = models.Article.objects(title="xx", text="nool")
    tes1.save()
## 一对多外键: 
        publiser_id = 2, 通过外联表的id关联
        publiser = pub[2], 必须跟对象
## 多对多: add增加, remove取消
    正向
        models.Article.authors.add(obj), 只能通过对象绑定
    反向
        author.article_set.add(*Article)  #Article大写变小写
# ------------------------------删
# 删除id=1的数据, 级联删除, 删除跟这个对象的所有信息
#1
    test1 = models.Article.objects.get(id=1)
    test1.delete()
#2
    models.Article.objects.filter(id=1).delete()
# 删除所有数据
    models.Article.objects.all().delete()
# ------------------------------改
# 修改id=1的title字段, 再save, 相当于 UPDATE
#1
    test1 = models.Article.objects.get(id=1)
    test1.title = 'Google'
    test1.save()
#2
    models.Article.objects.filter(id=1).update(title='Google')
# 修改所有的列
    models.Article.objects.all().update(title='Google')
# 去重
    models.Article.objects.all().distinct()
# ------------------------------查
# 获得所有数据, 相当于 SELECT * FROM
    list = models.Article.objects.all()        
# filter相当于 WHERE | 通过__隔开查询号和查询条件
    response2 = models.Article.objects.filter(id=1)
    response3 = models.Article.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的值
    models.Article.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
    models.Article.objects.exclude(id__in=[11, 22, 33])  # not in
# 获取单个对象
    response3 = models.Article.objects.get(id=1)     #获取对象, 不推荐, 其它方式都时获取的queryset
# 限制返回的数据 相当于 OFFSET 0 LIMIT 2;
    models.Article.objects.order_by('title')[0:2]
# 数据排序
    models.Article.objects.order_by("id")
    models.Article.objects.filter(name='seven').order_by('-id')   # desc
# regex正则匹配，iregex 不区分大小写
    models.Article.objects.get(title__regex=r'^(An?|The) +')
# 关联查询
    models.Article.objects.filter(author__id = 0).values('author__name')   #Article和Author关联表
# 聚合查询 aggregate
    from django.db.models import Avg, Min, Sum, Max
    models.Article.objects.all().aggregate(Avg('price'))    #在QuerySet上进行查询, 返回一个字典
# 分组查询 annotate
    models.Article.objects.all().annotate(Avg('price'))     #对结果分组, 返回多个字典组成的列表
# F查询 
    from django.db.models import F
    models.Article.objects.update( price = F('price') + 20)     #专门对对象的某列值进行操作
# Q查询
    from django.db.models import Q      #复杂多条件查询
    models.Article.objects.filter(Q(id = 3)|Q(price = '20'))  #或
    models.Article.objects.filter(Q(id = 3)&Q(price = '20'))  #并
    models.Article.objects.filter(~Q(price = '20'))           #非
    models.Article.objects.filter(~Q(price = '20'), title = 's')  #Q对象和条件混合, Q对象需要放前面
#---------------------------------------------------------------------------------------
'''