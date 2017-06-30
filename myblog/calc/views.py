#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.计算 You're at the polls index.") 
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    #return HttpResponse(str(c))
    context = {}
    context['c'] = c
    return render(request, 'add.html', locals())
