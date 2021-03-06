# Generated by Django 2.2.3 on 2019-11-01 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SyncRecoder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='名称')),
                ('alias', models.CharField(max_length=30, unique=True, verbose_name='别名')),
                ('describe', models.CharField(blank=True, max_length=100, null=True, verbose_name='描述')),
                ('status', models.CharField(max_length=30, verbose_name='更新状态')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('rate', models.CharField(default='5s', max_length=30, verbose_name='更新速率')),
                ('task', models.CharField(max_length=30, verbose_name='任务')),
                ('params', models.CharField(blank=True, max_length=1000, null=True, verbose_name='初始参数')),
                ('update', models.CharField(blank=True, max_length=1000, null=True, verbose_name='更新参数')),
                ('period', models.CharField(max_length=100, verbose_name='周期参数')),
                ('error', models.CharField(blank=True, max_length=1000, null=True, verbose_name='错误信息')),
            ],
            options={
                'verbose_name': '同步记录',
                'verbose_name_plural': '同步记录',
            },
        ),
    ]
