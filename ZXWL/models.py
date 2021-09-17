from django.db import models


class DynamicClass(models.Model):
    """ 动态类别 """
    name = models.CharField(max_length=50, verbose_name='动态名称')
    info = models.CharField(max_length=100, verbose_name='简介')  # 简介
    status = models.BooleanField(default=False, verbose_name='状态')  # 分类状态
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建日期', null=False)
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='修改日期', null=False)

    def __str__(self):
        return self.name


class DynamicDetail(models.Model):
    """动态详情"""
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    # cover = models.ImageField(verbose_name='封面', upload_to='media/upload/', null=False)
    overview = models.TextField(verbose_name='概述', null=False)
    status = models.BooleanField(default=True, verbose_name='文章状态')  # 文章状态
    is_hot = models.BooleanField(default=False, verbose_name='热点状态')  # 文章热点
    dynamic_class_id = models.ForeignKey(to='DynamicClass',
                                         verbose_name='类别外键',
                                         on_delete='CASCADE',
                                         related_name='class_dynamic')
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建日期', null=False)
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='修改日期', null=False)
