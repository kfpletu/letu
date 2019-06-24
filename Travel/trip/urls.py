from django.conf.urls import url

from trip.views import *

urlpatterns = [
    url(r'^$',trip_views),
]
