from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

g_count = 1

def f1(request):
    # x = {'a':1,'b':2}
    # 'a' not in x.keys()
    global g_count
    g_count += 1
    print('xxxxxx', g_count)
    # if request.META.has_key('HTTP_X_FORWARDED_FOR'):
    if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    print(ip)
    return HttpResponse('<h1>xxxxx</h1>')

print('***************** app1.views.py init do something **************************')