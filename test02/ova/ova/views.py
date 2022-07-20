from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request,'index.html',{})
def user(request, *args, **kwargs):
    return render(request,'user.html',{})
def product(request, *args, **kwargs):
    return render(request,'product.html',{})
def routine(request, *args, **kwargs):
    return render(request,'routine.html',{})
def membership(request, *args, **kwargs):
    return render(request,'membership.html',{})
def dance(request, *args, **kwargs):
    return render(request,'dances.html',{})
