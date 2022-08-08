from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ArticleModelSerializers, ArticlesDetailModelSerializers
from .models import Article


class CustomPagenation(PageNumberPagination):
    page_size = 10  # 每页最多显示记录
    page_query_param = 'page'  # ?page=2
    page_size_query_param = 'size'  # /list/?size=20
    max_page_size = 100  # 最大每页显示几条


class BlogView(ListAPIView):
    # permission_classes = [IsAdminUser, ]
    serializer_class = ArticleModelSerializers
    queryset = Article.objects.filter(is_deleted=False, is_show=True)

    # todo 设置添加博客文章后,自动创建文章互动表的数据


class BlogDetail(RetrieveAPIView):
    # 单片博客返回数据
    queryset = Article.objects.filter(is_deleted=False, is_show=True)
    serializer_class = ArticlesDetailModelSerializers
