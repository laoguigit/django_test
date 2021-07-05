from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def f1(request):
    # x = {'a':1,'b':2}
    # 'a' not in x.keys()

    print('xxxxxx')
    # if request.META.has_key('HTTP_X_FORWARDED_FOR'):
    if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    print(ip)
    return HttpResponse('<h1>xxxxx</h1>')