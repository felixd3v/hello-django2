from django.shortcuts import render
from django.http import HttpResponse #import

# Create your views here.
def home(request):
    return HttpResponse("Good morning, good afternoon, good evening. Nice to meet you!")

