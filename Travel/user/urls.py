from django.conf.urls import url
# from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$',views.index),
    # url(r'^admin/', admin.site.urls),
    url(r'^login', views.login,),
    url(r'^register', views.register),
    url(r'^cart',views.cart),
]
