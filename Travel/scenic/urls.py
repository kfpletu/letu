from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.add_scen,name='scenic1'),
    url(r'^ticket',views.ticket,name='ticket'),
    url(r'^scenic2',views.scenic2,name='scenic2'),
    url(r'^hf$',views.insert_scenic1),
]
