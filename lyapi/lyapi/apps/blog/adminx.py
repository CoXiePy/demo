import xadmin

from .models import Article, TagOfArticle,BlogComment


class ArticleModelAdmin(object):
    """模型管理类"""
    list_display = ['title', 'abstract', 'tags', 'is_show', 'is_deleted',"author"]


xadmin.site.register(Article, ArticleModelAdmin)
class BlogCommentModelAdmin(object):
    """模型管理类"""
    list_display = ['acticle', 'praise', 'reading', 'comments']


xadmin.site.register(BlogComment, BlogCommentModelAdmin)

class TagsModelAdmin(object):
    """模型管理类"""
    list_display = ['name', 'is_show']


xadmin.site.register(TagOfArticle, TagsModelAdmin)
