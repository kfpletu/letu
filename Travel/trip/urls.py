from django.conf.urls import url

from .views import *
#交通url分支
urlpatterns = [
    url(r'^$',trip_views),
    url(r'^search',search_views),
]
