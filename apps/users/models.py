from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名" )
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月" )
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机")
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female",u"女")),default="male", verbose_name="性别")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
