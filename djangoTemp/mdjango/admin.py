from django.contrib import admin
from .models import Article

# Register your models here.


#admin.site.register(Article, myadmin)  #注册内容 定制显示
class myadmin(admin.ModelAdmin):
    list_display = ("title", "price", "text")   #展示对象内容
    search_fields = ('title',)   #允许搜索范围
    list_filter = ('price',)    #允许筛选范围
    ordering = ('id',)      #允许排序类型