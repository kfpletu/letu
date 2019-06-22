from django.db import models

# Create your models here.

class Info(models.Model):
    uname = models.CharField('用户姓名', max_length=15)
    upwd = models.CharField('用户密码', max_length=15)
    phone = models.IntegerField('手机号')
    email = models.EmailField('邮箱')