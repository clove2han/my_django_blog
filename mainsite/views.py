#_*_coding:utf-8_*_

from django.shortcuts import render,render_to_response
from django.http import  HttpResponse
from .models import Post
from django.template.loader import get_template
from django.template import Template,Context
from datetime import datetime
#发生例外的时候直接返回首页。
from django.shortcuts import redirect
# Create your views here.


def homepage(request):
    template=get_template('index.html')
    posts=Post.objects.all()
    now=datetime.now()
    html=template.render(locals())
    return HttpResponse(html)
def showpost(request,slug):
    template=get_template('post.html')
    try:
        post=Post.objects.get(slug=slug)
        if post !=None:
            html=template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

def current_datetime(request):
    nowtime = datetime.now()
    # t =   Template("<html><body>It is now {{ current_datetime   }}.</body></html>")
    # html = t.render(Context({'current_datetime':nowtime}))
    return render_to_response('current_datetime.html',{'current_datetime':nowtime})