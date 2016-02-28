from django.contrib import admin

# Register your models here.
from article.models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)