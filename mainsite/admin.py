#_*_coding:utf-8_*_

from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')


#先导入post类，通过admain.site.register注册。
admin.site.register(Post,PostAdmin)