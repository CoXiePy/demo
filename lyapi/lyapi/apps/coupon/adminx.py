import xadmin
from . import models

import xadmin
from xadmin import views

class CouponModel(object):
    """Nav注册"""
    list_display = [ "name","coupon_type","timer","condition","sale"]


xadmin.site.register(models.Coupon, CouponModel)

class UserCouponModel(object):
    """Nav注册"""
    list_display = ["user", "coupon","start_time","is_use"]


xadmin.site.register(models.UserCoupon, UserCouponModel)