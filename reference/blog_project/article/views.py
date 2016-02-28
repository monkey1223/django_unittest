from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from article.models import Article, Comment
from django.http import HttpResponse

def articles(request):

    args = {}
    args.update(csrf(request))

    args['articles']    = Article.objects.all()
    args['logined_state'] = request.user.is_authenticated()

    return render_to_response('articles.html',
                                args)

def article(request, article_id=1):
    return render_to_response('article.html',
                                {'article':Article.objects.get(id=article_id) })

from article.forms import ArticleFrom, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def create(request):
    if request.user.is_authenticated():
        if request.POST:
            title = request.POST.get("title", "")
            content = request.POST.get("content", "")

            form = ArticleFrom(request.POST)

            if title.strip() == '' or content.strip() == '':
                pass

            elif form.is_valid():
                a = form.save(commit=False)
                a.creation_date = timezone.now()
                a.author = request.user
                a.save()

                return HttpResponseRedirect('/articles/all')
        else:
            form = ArticleFrom()
        args = {}
        args.update(csrf(request))
        args['form'] = form

        return render_to_response('create_article.html', args)
    else:
        return HttpResponseRedirect('/accounts/login')


from django.utils import timezone
def add_comment(request, article_id):
    if request.user.is_authenticated():
        a = Article.objects.get(id = article_id)

        if request.POST and request.POST.get("content", "").strip() != '':

            form = CommentForm(request.POST)

            if form.is_valid():
                c = form.save(commit=False)
                c.creation_date = timezone.now()
                c.article = a
                c.author = request.user
                c.save()

                return HttpResponseRedirect('/articles/get/%s' % article_id)
        else:
            form = CommentForm()

        args = {}
        args.update(csrf(request))

        args['article'] = a
        args['form'] = form

        return render_to_response('add_comment.html', args)
    else:
        return HttpResponseRedirect('/accounts/login')