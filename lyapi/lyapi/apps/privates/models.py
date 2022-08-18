# import datetime
#
# from django.db import models
# from mdeditor.fields import MDTextField
# from lyapi.utils.models import BaseModel
#
#
# class Article(BaseModel):
#     author = models.ForeignKey(to="users.User", related_name="author_name", verbose_name="作者名称",
#                                on_delete=models.DO_NOTHING)
#     title = models.CharField(max_length=200, verbose_name="博客标题")
#     abstract = models.CharField(max_length=200, verbose_name="博客摘要")
#     content = MDTextField(verbose_name="文章内容")  # 这个字段后台用markdown编辑器来展示
#     tags = models.ManyToManyField(to="TagOfArticle", related_name="tag_articles", verbose_name="文章标题")
#
#     def __str__(self):
#         return self.title
#
#     @property
#     def author_name(self):
#         """
#         返回昵称的函数
#         """
#         name = self.author.userinfo.filter(is_show=True, is_deleted=False).first().nickname
#         return name
#
#     @property
#     def tags_data(self):
#         name = self.tags.filter(is_show=True, is_deleted=False).values("name")
#         return name
#
#     class Meta:
#         db_table = "b_blog"
#         verbose_name = "博客文章"
#         verbose_name_plural = verbose_name
#
#
#
#
# class TagOfArticle(BaseModel):
#     name = models.CharField(max_length=255, verbose_name="文章标签1")
#
#     def __str__(self):
#         return self.name
#
#     def related_article_num(self):
#         return Article.objects.filter(tags=self).count()
#
#     class Meta:
#         db_table = 'b_pri'
#         verbose_name = '私人技术'
#         verbose_name_plural = verbose_name