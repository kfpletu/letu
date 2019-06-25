from django.http import HttpResponse
from django.shortcuts import render, redirect
from .trail_12306 import *


# Create your views here.
def trip_views(request):
    return render(request, 'trip/order.html')


def search_views(request):
    if request.method == "GET":
        from_station = request.GET.get('from_city', '')
        to_station = request.GET.get('to_city', '')
        from_date = request.GET.get('from_day', '')
        to_date = request.GET.get('to_day', '')
        # print(type(from_station))
        # print(from_station,to_station,from_date,to_date)
        tt = TicketQuery()
        data = tt.query(from_station, to_station, from_date)
        print(data)
        return render(request, 'trip/new_order.html', locals())
    elif request.method == "POST":
        return HttpResponse("没有这项服务")
