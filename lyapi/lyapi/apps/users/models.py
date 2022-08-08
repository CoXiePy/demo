from django.contrib.auth.models import AbstractUser
from django.db import models
from lyapi.utils.models import BaseModel


# Create your models here.


class User(AbstractUser):
    wechat = models.CharField(max_length=20, null=True, default=None, verbose_name="微信号")
    mobile = models.CharField(max_length=11, null=True, default=None, verbose_name="手机号")

    class Meta:
        db_table = "b_user"
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name

class UserInfo(BaseModel):
    user = models.ForeignKey(to="users.User",related_name="userinfo", verbose_name="用户帐号",default=1,  on_delete=models.DO_NOTHING)
    nickname = models.CharField(max_length=30, verbose_name="昵称", default="该用户很懒没有设置昵称", null=True)

    class Meta:
        db_table = "b_userinfo"
        verbose_name = "用户详情表"
        verbose_name_plural = verbose_name

