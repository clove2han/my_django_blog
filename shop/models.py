#_*_coding:utf-8_*_
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

# Create your models here.
#创建产品分类模型

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta:
        ordering =('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])

#创建产品模型
class Product(models.Model):

    # 这是一个链接向Category的ForeignKey,
    # 这是多对一关系，一个产品可以属于一个分类，一个分类可以包含多个产品
    category = models.ForeignKey(Category,related_name='products')

    #这是产品的名字
    name = models.CharField(max_length=200,db_index=True)

    #用来为产品建立URL的slug
    slug = models.SlugField(max_length=200,db_index=True)

    #可选的产品图片
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)

    #可选的产品描述
    description = models.TextField(blank=True)

    #这是产品价格，保存一个固定精度的十进制数，最大十位数，小数精确到两位
    price = models.DecimalField(max_digits=10,decimal_places=2)

    #用正整数保存产品的库存
    stock = models.PositiveIntegerField()

    #产品是否可供购买，可以在目录中使产品废弃或生效
    available = models.BooleanField(default=True)

    #创建时间， 当对象被创建时 自动生成
    created = models.DateTimeField(auto_now=True)

    #修改时间，保存最后一次更新的时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',args=[self.id,self.slug])
