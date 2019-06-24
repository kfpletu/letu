from django.conf.urls import url

from trip.views import *
#交通url分支
urlpatterns = [
    url(r'^$',trip_views),
]
