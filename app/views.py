from django.shortcuts import render, HttpResponse

from .tasks import sleepy # Imports the background task function

# Create your views here.

def index(request):
    sleepy.delay(10)
    return HttpResponse('<h1>Task is Done!</h1>')