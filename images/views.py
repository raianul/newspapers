from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def response_images(request):
    return HttpResponse("Hi, I am in Images !!")