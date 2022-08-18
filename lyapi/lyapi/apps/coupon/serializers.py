from rest_framework import serializers
from . import models


# 嵌套的序列化器
class CouponModelSerilizer(serializers.ModelSerializer):
    class Meta:
        model = models.Coupon
        fields = ['name', 'condition', 'sale', 'coupon_type']


class UserCouponModelSerializer(serializers.ModelSerializer):
    # 前端需要获取 ，优惠券名，优惠券开始时间，优惠券过期时间，优惠券id，优惠券条件
    coupon = CouponModelSerilizer()
    class Meta:
        model = models.UserCoupon
        fields = ['id','start_time', 'end_time', 'coupon' ]