from django.shortcuts import render
from django.http import HttpResponse

from .tasks import sleepy

# Create your views here.

def index(request):
    sleepy.delay(10)
    return HttpResponse('<h1>Task is Done!</h1>')