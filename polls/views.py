from django.urls import path
from django.http import HttpResponse
# Create your views here.

def macbook(request):
    return HttpResponse('This is MacBook')

def hp(request):
    return HttpResponse('This is HP')    

def asus(request):
    return HttpResponse('This is Asus')

def detail(request, noutbook_id):
    return HttpResponse(f'Your noutbook is {noutbook_id}')   