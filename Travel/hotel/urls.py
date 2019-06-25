from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    # url(r'(\d{2})',views.test),
    url(r'^(\d+)$',views.hotel),
    # url(r'init',views.init_db)
]
