#_*_coding:utf-8_*_

from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse
from django.http import  HttpResponse,HttpResponseRedirect
from models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect
from forms import MomentForm
import os
from django.views.decorators.csrf import csrf_exempt

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
@csrf_exempt
def moments_input(request):

    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():

            moment = form.save()
            moment.save()

            return HttpResponseRedirect(reverse('welcome'))   #这里的名称是url name
    else:
        form = MomentForm()
    # form = MomentForm()
    PROJECT_ROOT =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request,os.path.join(PROJECT_ROOT,'mainsite/templates','input.html'),{'form':form})