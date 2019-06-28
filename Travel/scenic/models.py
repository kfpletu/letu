from django.db import models
# from ..user.models import Info
# Create your models here.
class Scenic1(models.Model):
    sce_name=models.CharField('景点名称',max_length=8,unique=True)
    sce_topic=models.CharField('主题名称',max_length=15)
    brief_des=models.CharField('景点简述',max_length=40)
    bus_go=models.CharField('公交',max_length=40)
    car_go=models.CharField('自驾',max_length=40)
    pre_price=models.DecimalField("原价",max_digits=6,decimal_places=2)
    local_price=models.DecimalField("现价",max_digits=6,decimal_places=2)
    rebate=models.FloatField("折扣率",null=True)
    low_time=models.DateField("优惠截止时间",default='2019-9-20')

    grage=models.CharField('景区级别',default='AAAA',max_length=10)
    sce_address=models.CharField("景区地址",max_length=15)
    open_time=models.CharField("开放时间",max_length=200)
    img_1=models.ImageField('景点图片1')
    img_2=models.ImageField('景点图片2')
    img_3=models.ImageField('景点图片3')
    img_4=models.ImageField('景点图片4')
    img_5=models.ImageField('景点图片5')
    word1=models.CharField('主题词1',max_length=5,null=True)
    word2=models.CharField('主题词1',max_length=5,null=True)
    word3=models.CharField('主题词1',max_length=5,null=True)
    class Meta:
        verbose_name='景点信息表'
        verbose_name_plural = verbose_name
class Introduce(models.Model):
    sce_details=models.TextField('景区介绍')
    sce_name2=models.OneToOneField(Scenic1)
class Address(models.Model):
    longitudes=models.DecimalField('经度',max_digits=9,decimal_places=6)
    latitudes=models.DecimalField('纬度',max_digits=8,decimal_places=6)
    sce_name2 = models.OneToOneField(Scenic1)
class Ticket(models.Model):
    ticket_type=models.CharField("门票种类",max_length=10)
    ticket_name=models.CharField("门票名称",max_length=20)
    ticket_price=models.DecimalField("门票价格",max_digits=6,decimal_places=2)
    sce_name3 = models.ForeignKey(Scenic1)

# class Preorder_list(models.Model):
#     auto_time=models.DateField("加入购物车时间",auto_now_add=True)
#     order_ticket = models.ForeignKey(Ticket)
#     order_time = models.DateField("游玩时间",null=True)
#     order_sum=models.IntegerField("订票数量",null=True)
#     order_money=models.DecimalField("金额",max_digits=6,decimal_places=2,null=True)
#     order_user = models.ForeignKey(Info)



