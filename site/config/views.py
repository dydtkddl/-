from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from article.models import *
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')
def signup(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        User(email=email, name=name, pwd=pwd).save()
        return render(request,'signup.html')
    else:
        return render(request, 'signup.html')
def searchuserinfo(request):
    