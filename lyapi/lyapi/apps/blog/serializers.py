from rest_framework import serializers
from . import models


class BlogComments(serializers.ModelSerializer):
    # 文章互动数据返回
    class Meta:
        model = models.BlogComment
        fields = ["praise", "reading", "comments"]


class ArticleModelSerializers(serializers.ModelSerializer):
    blog_comment = BlogComments()

    # 所有文章数据返回
    class Meta:
        model = models.Article
        fields = ["id", "title", "abstract", "updated_time", "tags_data", "author", "author_name", "blog_comment", ]


class ArticlesDetailModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ["id", "title", "abstract", "content", "updated_time", "tags_data", "author", "author_name",
                  "re_blog_comment"]