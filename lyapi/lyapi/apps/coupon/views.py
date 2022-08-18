import datetime
# Create your views here.
from rest_framework.generics import ListAPIView
from . import models
from .serializers import UserCouponModelSerializer
from rest_framework.permissions import IsAuthenticated


class CouponView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserCouponModelSerializer
    # queryset = models.UserCoupon.objects.filter(
    #     is_show=True,
    #     is_deleted=False,
    #     is_use=False,
    #     user=2,
    # )
    def get_queryset(self):
        now = datetime.datetime.now()
        print(self.request)
        queryset = models.UserCoupon.objects.filter(
            is_show=True,
            is_deleted=False,
            is_use=False,
            user=self.request.user,
            start_time__lte=now,  # 已经开始的
        )
        return queryset
