from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
        

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
