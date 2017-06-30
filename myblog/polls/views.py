#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.问候 You're at the polls index.")
def home(request):
    return render(request, 'home.html')

