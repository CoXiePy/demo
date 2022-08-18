import xadmin
from . import models

import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "CoXIe博客后台管理"  # 设置站点标题
    site_footer = "个人站点"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)

class UserInfo(object):
    list_display = ["nickname", 'user']

xadmin.site.register(models.UserInfo, UserInfo)

