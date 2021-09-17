from django.db import models

# Create your models here.


class ClienteleInfos(models.Model):
    name = models.CharField(max_length=5, verbose_name='姓名')
    card = models.CharField(max_length=20, verbose_name='身份证号')
    mobile = models.CharField(max_length=11, verbose_name='手机号')

    class Meta:
        verbose_name = '客户信息'
        verbose_name_plural = verbose_name
