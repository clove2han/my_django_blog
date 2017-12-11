#_*_coding:utf-8_*_
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    #显示文章的标题
    title=models.CharField(max_length=200,verbose_name='标题')
    #显示文章的网址
    slug= models.CharField(max_length=200)
    #显示文章的内容
    body= models.TextField()
    #文章发表的时间,默认为现在时间。
    pub_date=models.DateTimeField(default=timezone.now)
    #此设置是说文章的显示顺序要按照pub_date的顺序来执行
    class Meta:
        ordering=('-pub_date',)
        verbose_name = '博客'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title

KIND_CHOICES =(
    ('Python技术','Python技术'),
    ('数据库技术','数据库技术'),
    ('经济学','经济学'),
    ('其他','其他'),
)
# Create your models here.

class Moment(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20,default='匿名')
    kind = models.CharField(max_length=20,choices=KIND_CHOICES,default = KIND_CHOICES[0])

