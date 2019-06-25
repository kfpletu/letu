from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name=models.CharField('酒店名字',max_length=20)
    address=models.CharField('酒店地址',max_length=100)
    phone=models.CharField('酒店电话',max_length=20)
    info=models.TextField('酒店详细信息')
    hotel_p11=models.ImageField('酒店图片1')
    hotel_p12=models.ImageField('酒店图片2')
    hotel_p13=models.ImageField('酒店图片3')
    hotel_p14=models.ImageField('酒店图片4')
    hotel_p15=models.ImageField('酒店图片5')
    hotel_level=models.CharField('酒店级别',max_length=10)

    def __str__(self):
        return "酒店名：%s 酒店电话：%s 酒店地址：%s"%(self.hotel_name,self.phone,self.address)

