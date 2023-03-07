from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def raj(request):
    return HttpResponse('<h1> i am good boy </h1>')