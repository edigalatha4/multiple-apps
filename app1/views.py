from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>This is first view in app1</h1>')

def second(request):
    return HttpResponse('<h1><b>This is second view in app1</b></h1>')
