from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hello World")
def item(request):
    return HttpResponse('<h1>This is an item view</h1>')


# Create your views here.
