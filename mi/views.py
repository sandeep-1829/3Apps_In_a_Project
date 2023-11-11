from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def rohit(request):
    return render(request,'rohit.html')


def sky(request):
    return HttpResponse('<h1>Indian 360* Player...</h1>')