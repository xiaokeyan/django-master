from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    auth = models.CharField(
        max_length=50, verbose_name='权限认证', default=[0, 0, 0, 0]
    )  # ['人事'， ‘艺术团’， ‘剧场’， ‘财务’]
    name = models.CharField(verbose_name='昵称', max_length=10)
    username = models.CharField(max_length=20, verbose_name='用户名', unique=True, null=False)
    password = models.CharField(max_length=180, verbose_name='密码', null=False)
    is_superuser = models.BooleanField(default=False, verbose_name='管理员')
    date_joined = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_user_dict(self):
        return {
            'name': self.name,
            'is_superuser': self.is_superuser,
            'username': self.username,
            'auth': self.auth
        }


class WorkerUser(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=120)
    mail = models.EmailField()
    ctime = models.DateTimeField(auto_now=True)
    status = models.IntegerField()
    sort = models.IntegerField()
    jobs = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    usercard = models.CharField(max_length=20)
    jobnature = models.CharField(max_length=20)
    tryout = models.IntegerField()
    usernumber = models.IntegerField()
    deleted = models.CharField(max_length=20)
    years = models.CharField(max_length=20)
    month = models.CharField(max_length=20)
    day = models.CharField(max_length=20)
    zzface = models.CharField(max_length=20)
    ztimeday = models.IntegerField()
    ztime = models.CharField(max_length=20)
    lztime = models.CharField(max_length=20)
    salary = models.FloatField()
    sysalary = models.FloatField()
    sbbase = models.FloatField()
    gjjbase = models.FloatField()
    znedu = models.FloatField()
    jxedu = models.FloatField()
    zfdklx = models.FloatField()
    zfzj = models.FloatField()
    dbyl = models.FloatField()
    sylr = models.FloatField()
