from django.shortcuts import render
from django.http import HttpResponsepython
# Create your views here.


def home(request):
    return HttpResponse("hello World")
