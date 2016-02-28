from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Article(models.Model):
    title       = models.CharField(max_length=200)
    content     = models.TextField()
    creation_date = models.DateTimeField('date published')
    author      = models.ForeignKey(User, verbose_name=_("author"))

    def __unicode__(self):
        return self.title

    # for test. if you want to test urls|view|api, it must be this.
    def get_absolute_url(self):
        return '/articles/get/%i/' % self.id # this is error  Change into " ' /articles/get/%i/' "

class Comment(models.Model):
    # content =
    # creation_date =
    # article =
    # author  =
	pass
