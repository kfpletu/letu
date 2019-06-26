from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse

# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取登录页面form表单提交的uname和upwd
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')

        # 获取验证码
        validateCode = request.POST.get('validateCode')


        # 从数据库获取uname和upwd
        infos = Info.objects.values('uname', 'upwd')
        # 循环判断输入的uname和upwd是否相等
        for info in infos:
            if uname==info['uname'] and upwd==info['upwd']:
                return render(request,'index.html',locals())
            else:
                continue
        # 循环完所有结果,说明用户名密码不正确,刷新当前登录页面
        return render(request,'user/login.html')

#注册
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        # 获取用户注册输入的信息
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        # 获取数据库uname,判断是否重复
        if Info.objects.filter(uname=uname):
            return render(request, 'user/register.html', locals())
        else:
            newinfo = Info(uname=uname, upwd=upwd, phone=phone, email=email)
            newinfo.save()
            return render(request, 'index.html', locals())

#购物车
def cart(request):
    return render(request,'user/cart.html')
#历史记录
def order(request):
    return render(request,'user/order.html')



# 忘记密码
def forget(request):
    if request.method == 'GET':
        return render(request, 'user/forget.html')
    elif request.method == 'POST':

        # 获取用户输入的信息
        uname = request.POST.get('uname') # 用户名
        phone = request.POST.get('phone') # 电话号码
        email = request.POST.get('email') # 邮箱
        validateCode = request.POST.get('validateCode') # 验证码
        
        return render(request, 'user/forget_new.html')

def getpwd(request):
    if request.method == 'GET':
        return render(request, 'user/forget.html')
    elif request.method == 'POST':

        # 获取用户输入的新密码
        new_pwd = request.POST.get('new_pwd')
        new_pwd_again = request.POST.get('new_pwd_again')
        
        
        return render(request, 'user/login.html')
        
