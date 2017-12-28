# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin
from bookapp.models import *

class BookAdmin(admin.ModelAdmin):
    list_display =('isbn','title','subtitle','pages','author','translator','publisher','pubdate')
    list_filter = ('author','publisher',)
    search_fields = ('id','title','isbn')
    list_per_page=20
admin.site.register(Book,BookAdmin)