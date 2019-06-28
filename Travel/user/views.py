from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# 登录
def login(request):
    if request.method == 'GET':
        print('get')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取登录页面form表单提交的uname和upwd
        print('post')
        uname = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        # 获取验证码
        validateCode = request.POST.get('validateCode')

        # 从数据库获取uname和upwd
        print('try外')
        try:
            print('try里面')
            user = Info.objects.get(uname=uname, upwd=upwd)
            request.session['userinfo'] = {
                'uname': user.uname,
                'id': user.id
            }
            # if remember:
            #     resp.set_cookie('uname', uname, max_age=7 * 24 * 60 * 60)
            # else:
            #     resp.delete_cookie('uname')
            print('2')
            return render(request, 'index.html', locals())
        except:
            # 出异常,说明用户名密码不正确,刷新当前登录页面
            print('1')
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

def index(request):
    uname=''
    return render(request, 'index.html', locals())

# 忘记密码
def forget(request):
    return render(request,'user/forget.html')

#购物车
def cart(request):
    
    return render(request,'user/cart.html')

#历史记录
def order(request):
    return render(request,'user/order.html')
