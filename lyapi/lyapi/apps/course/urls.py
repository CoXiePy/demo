from django.urls import path, re_path
from . import views

urlpatterns = [
    path('categorys/', views.CourseCategoryView.as_view()),
    path('list/', views.CourseListView.as_view()),  # 获取课程的信息
    re_path("(?P<pk>\d+)/", views.CourseRetrieveAPIView.as_view()),
    re_path("detail/(?P<pk>\d+/)", views.CourseCDetailListAPIView.as_view()),
    re_path("chapter/", views.ChapterListView.as_view()),
]
