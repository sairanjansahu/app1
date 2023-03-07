from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def swaraj(request):
    return HttpResponse('I LOVE MY INDIA')