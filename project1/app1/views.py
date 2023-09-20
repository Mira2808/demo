from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ("<h1>this is index</h1>")
def products(request):
    return HttpResponse ("<h1>this is index</h1>")
