from tastypie.resources import ModelResource
from tastypie.constants import ALL
from article.models import Article, Comment

class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = {"title": ALL}# http://localhost:8000/articles/api/article/?format=xml&title__contains=icl

class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        filtering = {"content": ALL}
