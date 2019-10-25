from django.db import models
from celery.task import Task


# Create your models here.
class SyncRecoder(models.Model):
    '''
    使用方式，通过装饰方法Record对task进行装饰，
    '''
    name = models.CharField(
        max_length=30, blank=False, verbose_name='名称', primary_key=True)
    alias = models.CharField(
        max_length=30, blank=False, verbose_name='别名', unique=True)
    describe = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='描述')
    status = models.CharField(max_length=30, verbose_name='更新状态')
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 更新速率表示，该任务间隔多长时间去请求一次
    rate = models.CharField(max_length=30, verbose_name='更新速率', default='5s')
    # task = models.OneToOneField(Task,on_delete=models.CASCADE, verbose_name='任务')
    task = models.CharField(
        max_length=30, blank=False, null=False, verbose_name='任务')
    params = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name='初始参数')
    update = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name='更新参数')
    period = models.CharField(max_length=100, verbose_name='周期参数')
    error = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name='错误信息')

    class Meta:
        verbose_name = "同步记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
