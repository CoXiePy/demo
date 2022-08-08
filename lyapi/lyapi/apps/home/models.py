from django.db import models
from lyapi.utils.models import BaseModel
# Create your models here.

class Nav(BaseModel):
    """导航菜单模型"""
    POSITION_OPTION = (
        (1, "顶部导航"),
        (2, "脚部导航"),
    )
    title = models.CharField(max_length=500, verbose_name="导航标题")
    link = models.CharField(max_length=500, verbose_name="导航链接")
    position = models.IntegerField(choices=POSITION_OPTION, default=1, verbose_name="导航位置")
    is_site = models.BooleanField(default=False, verbose_name="是否是站外地址")

    class Meta:
        db_table = 'ly_nav'
        verbose_name = '导航菜单'
        verbose_name_plural = verbose_name

    # 自定义方法[自定义字段或者自定义工具方法]
    def __str__(self):
        return self.title