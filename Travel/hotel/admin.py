from django.contrib import admin
from . import models
# Register your models here.


class HotelManager(admin.ModelAdmin):
    list_display = ['id','hotel_name']
    # list_editable = ['id','hotel_name']


class RoomManager(admin.ModelAdmin):
    list_display = ['id','room_name','hotel_id']
    # list_editable = ['room_name']
    list_display_links=['room_name']

admin.site.register(models.Hotel,HotelManager)
admin.site.register(models.Room,RoomManager)