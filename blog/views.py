from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('欢迎使用Django！')
