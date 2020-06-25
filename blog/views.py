from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,template_name='index.html')


def single(request):
    return render(request, template_name='single.html')
