from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    form = RegisterForm()
    return render(request, 'register.html',{'form':form})

def test(request):
    return render(request,"test.html")