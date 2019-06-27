from django.db import models

# Create your models here.

class Info(models.Model):
    uname = models.CharField('用户姓名', max_length=15,unique=True)
    upwd = models.CharField('用户密码', max_length=15,null=False)
    phone = models.CharField('手机号', max_length=11, unique=True)
    email = models.EmailField('邮箱')


# class Cart(models.Model):
    # ticket = models.ForeignKey(Ticket)
    # user = models.ForeignKey(User)
    # good = models.ForeignKey(Good)  


# class Order(models.Model):
    # count = models.IntergerField('数量',default=1)
	# #total_price = models.DecimalField('总金额',max_digits=10,decimal_places=2)
    # pay_time = models.DateTimeField(auto_now_add=True)
    # cart = models.ForeignKey(Cart)
    

   