from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'(\d{2})',views.test),
    url(r'^31$',views.fu_li_xi_er_dun)
]
