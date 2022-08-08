from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.BlogView.as_view()),  # 获取所有文章列表数据
    path("blog_list/", views.BlogView.as_view()),  # 获取所有文章列表数据
    re_path(r'detail/(?P<pk>\d+)/', views.BlogDetail.as_view()),  # 获取单个文章列表数据
]