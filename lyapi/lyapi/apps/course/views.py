from django.shortcuts import render

# Create your views here.
from . import models
from .models import Course, CourseChapter
from .serializers import CourseCategoryModelSerializer, CourseModelSerializer, \
    CourseRetrieveSerializer, CourseDetailModelSerializer, ChapterModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView, ListAPIView

# 分页
class CustomPagenation(PageNumberPagination):
    page_size = 5  # 没页显示5条记录
    page_query_param = 'page'  # ?page=2
    page_size_query_param = 'size'  # /list/?size=20
    max_page_size = 100  # 最大每页显示几条

# 获取课程章节信息 1
class CourseCategoryView(ListAPIView):
    queryset = models.CourseCategory.objects.filter(is_show=True, is_deleted=False)
    serializer_class = CourseCategoryModelSerializer

# 2
class CourseListView(ListAPIView):
    queryset = models.Course.objects.filter(is_show=True, is_deleted=False)
    serializer_class = CourseModelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('course_category',)
    pagination_class = CustomPagenation

# class CourseListView(ListAPIView):
#     queryset = models.Course.objects.filter(is_show=True, is_deleted=False)
#     serializer_class = CourseModelSerializer


# 获取课程的单挑记录 ，前端传惨： 课程id 4
class CourseCDetailListAPIView(RetrieveAPIView):
    queryset = models.Course.objects.filter(is_show=True, is_deleted=False)
    serializer_class = CourseDetailModelSerializer



# 3
class CourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.filter(is_deleted=False, is_show=True)
    serializer_class = CourseRetrieveSerializer


# 获取章节数据的试图 5
class ChapterListView(ListAPIView):
    queryset = models.CourseChapter.objects.filter(is_show=True, is_deleted=False)
    serializer_class = ChapterModelSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_fields = ('course',)
    #  /course/chapter/?course=2