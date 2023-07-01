from django.shortcuts import render
#from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('topic is inserted')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WPO=WebpageForm()
    d={'WPO':WPO}

    if request.method=='POST':
        WFO=WebpageForm(request.POST)
        if WFO.is_valid():
            WFO.save()
            return HttpResponse('webpage is submitted')
    return render(request,'insert_webpage.html',d)

def insert_access(requst):
    AO=AccessForm()
    d={'AO':AO}

    if requst.method=='POST':
        AFO=AccessForm(requst.POST)
        if AFO.is_valid():
            AFO.save()
            return HttpResponse('Access is inserted')
    return render(requst,'insert_access.html',d)