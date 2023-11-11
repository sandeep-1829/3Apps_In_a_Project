from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def virat(request):
    return render(request,'virat.html')


def maxwell(request):
    return HttpResponse('<h1>***Flexible Batter...And His batting Is Tremendous...***</h1>')