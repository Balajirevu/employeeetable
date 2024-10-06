from django.shortcuts import render
from .models import *

# Create your views here.
def emplist(request):
    return render(request,'list.html')
def empform(request):
    return render (request,'form.html')
def empdel(request):
    return