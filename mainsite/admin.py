#_*_coding:utf-8_*_

from django.contrib import admin
from .models import Post,Category,Product
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

#先导入post类，通过admain.site.register注册。
admin.site.register(Post,PostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','stock','available']  #可被编辑的字段
    prepopulated_fields = {'slug':('name',)}      #自动赋值的字段

admin.site.register(Product,ProductAdmin)
