from django.shortcuts import render

# Create your views here.
def trip_views(request):
    return render(request,'trip/order.html')