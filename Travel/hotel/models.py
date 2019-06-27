from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name=models.CharField('酒店名字',max_length=20)
    address=models.CharField('酒店地址',max_length=100)
    phone=models.CharField('酒店电话',max_length=50)
    info=models.TextField('酒店详细信息')
    hotel_level=models.CharField('酒店级别',max_length=10)
    class Meta:
        db_table='hotel'


    def __str__(self):
        return "酒店名：%s 酒店电话：%s 酒店地址：%s"%(self.hotel_name,self.phone,self.address)


class Room(models.Model):
    room_name=models.CharField('房间名',max_length=20)
    area=models.CharField('面积',max_length=10)
    price=models.CharField('价位',max_length=10)
    window=models.CharField('窗',max_length=20)
    bed=models.CharField('床',max_length=100)
    hotel=models.ForeignKey(Hotel,null=True)
    class Meta:
        db_table='room'

    def __str__(self):
        return '房间名: %s 价位: %s'%(self.room_name,self.price)