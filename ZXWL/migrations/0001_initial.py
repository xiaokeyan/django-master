# Generated by Django 2.2.5 on 2021-08-30 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='动态名称')),
                ('info', models.CharField(max_length=100, verbose_name='简介')),
                ('status', models.BooleanField(default=False, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='修改日期')),
            ],
        ),
        migrations.CreateModel(
            name='DynamicDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='正文')),
                ('cover', models.ImageField(upload_to='media/upload/', verbose_name='封面')),
                ('overview', models.TextField(verbose_name='概述')),
                ('status', models.BooleanField(default=True, verbose_name='文章状态')),
                ('is_hot', models.BooleanField(default=False, verbose_name='热点状态')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建日期')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='修改日期')),
                ('dynamic_class_id', models.ForeignKey(on_delete='CASCADE', related_name='class_dynamic', to='ZXWL.DynamicClass', verbose_name='类别外键')),
            ],
        ),
    ]
