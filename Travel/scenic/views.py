from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    return render(request,'scenic/information.html')
def ticket(request):
    return render(request,'scenic/ticket.html')
def scenic2(request):
    return render(request,'scenic/information02.html')