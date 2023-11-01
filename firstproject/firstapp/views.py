from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    x="Welcome to Nihar Sir...."
    return HttpResponse(x)