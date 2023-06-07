from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')

def lgout(request):
    return render(request,'index.html')

def dt(request):
    return render(request,'detail.html')