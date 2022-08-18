import xadmin
from . import models

import xadmin
from xadmin import views

class NavModel(object):
    """Nav注册"""
    list_display = ["title", "link","position","is_site"]


xadmin.site.register(models.Nav, NavModel)