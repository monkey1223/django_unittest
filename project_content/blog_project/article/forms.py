from django import forms
from article.models import Article, Comment

class ArticleFrom(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    pass