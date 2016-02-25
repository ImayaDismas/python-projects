from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def foo(request):
    name = "Dismas"
    html = "<html><body><h1>Hello World! from %s</h1></body></html>" % name
    return HttpResponse(html)