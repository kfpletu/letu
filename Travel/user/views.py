from django.shortcuts import render

# Create your views here.
from .models import *

# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

#注册
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        return

#购物车
def cart(request):
    return render(request,'user/cart.html')


def index(request):
    if request.method == 'GET':
        uname=''
        return render(request, 'index.html', locals())
    elif request.method == 'POST':
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        newinfo = Info(uname=uname, upwd=upwd, phone=phone, email=email)
        if Info.objects.filter(uname=uname):
            return render(request, 'index.html', locals())
        else:
            newinfo.save()
            print('uname:',uname)
            return render(request, 'index.html', locals())
