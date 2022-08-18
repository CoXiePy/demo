# from django.contrib.auth.backends import ModelBackend
# from django.db.models import Q
# from . import models
#
#
# def jwt_response_payload_handler(token, user=None, request=None):
#     return {
#         'token': token,
#         'id': user.id,
#         'username': user.username
#     }
#
#
# def get_user_by_backend(account):
#     try:
#         user = models.User.objects.get(Q(username=account) | Q(tel=account))
#         return user
#     except models.User.DoesNotExist:
#         return None
#
# class MyModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         user = get_user_by_backend(username)
#         if user:
#             if user.check_password(password):
#                 return user

from lyapi.settings.contains import CREDIT_MONEY
from django.conf import settings
from django_redis import get_redis_connection


def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    token:  jwt 字符串
    user: 当前登录用户对象
    request: 当前请求对象
    """
    user_id = user.id
    # conn = get_redis_connection('cart')
    # cart_length = conn.hlen(user_id)
    return {
        'token': token,
        'id': user_id,
        'username': user.username,
        # 'cart_length': cart_length,
        'credit': user.credit,
        "credit_to_money": CREDIT_MONEY,
    }


def get_user_by_backend(account):
    try:
        user = models.User.objects.get(Q(username=account) | Q(tel=account))

        return user
    except models.User.DoesNotExist:
        return None


def get_email_by_backend(account):
    try:
        email = models.User.objects.get(Q(email=account))
        return True
    except models.User.DoesNotExist:
        return False


from urllib.parse import urlencode
from urllib.request import urlopen
import json
import logging

logger = logging.getLogger('django')


def txrequest(Ticket, Randstr, UserIP):
    params = {
        "aid": settings.TENCENT_CAPTCHA.get('APPID'),
        "AppSecretKey": settings.TENCENT_CAPTCHA.get('App_Secret_Key'),
        "Ticket": Ticket,
        "Randstr": Randstr,
        "UserIP": UserIP
    }
    url = settings.TENCENT_CAPTCHA.get('GATEWAY')
    params = urlencode(params).encode()
    f = urlopen(url, params)

    content = f.read()
    res = json.loads(content)  # {response:“1”, evil_level:70, err_msg:""}
    print(res)  # {'response': '1', 'evil_level': '0', 'err_msg': 'OK'}
    if res:
        error_code = res["response"]
        if error_code == '1':
            return True
        else:
            # print("%s:%s" % (res["response"],res["err_msg"]))
            logger.warning("%s:%s" % (res["response"], res["err_msg"]))
            return False
    else:
        logger.warning("验证票据的响应数据有问题")

        return False


from . import models
from django.db.models import Q
from django.contrib.auth.backends import ModelBackend


class CustomModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        # username可能是手机号，可能是用户名
        # requests.post()
        ticket = kwargs.get('ticket')
        if ticket:  # 获取不到ticket表示，是xadmin登录认证
            randstr = kwargs.get('randstr')
            user_ip = request.META.get('REMOTE_ADDR')
            ret = txrequest(ticket, randstr, user_ip)
            # print('1111111', ticket, randstr, user_ip)
            if ret:

                user = get_user_by_backend(username)
                if user:

                    if user.check_password(password):
                        return user

        else:
            # print('>>>>>>>',username, password)
            ret = super().authenticate(request, username=username, password=password, **kwargs)
            return ret
