# todo 解决jwt问题
from rest_framework_jwt.serializers import jwt_decode_handler
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer

class LoginView(JSONWebTokenAPIView):
    permission_classes = JSONWebTokenSerializer

