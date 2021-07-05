from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f1(request):
    print('xxxxxx')
    return HttpResponse('<h1>xxxxx</h1>')