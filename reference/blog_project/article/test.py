from django.test import TestCase
from django.test.client import Client
# Create your tests here.
from article.models import  Article, Comment
from django.contrib.auth.models import User
from django.utils import timezone
from time import time
from django.core.urlresolvers import reverse

class ArticleTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', email='test@hotmail.com', password='test_pwd')
        self.user.save()

    def create_article(self, title="test article", content="test content"):

        # self.client.login(username='test_user', password='test_pwd')


        return Article.objects.create(title         = title,
                                      content       = content,
                                      creation_date = timezone.now(),
                                      author        = self.user)

    def test_article_creation(self):
        a = self.create_article()
        self.assertTrue(isinstance(a, Article))
        self.assertEqual(a.__unicode__(), a.title)

    def test_articles_list_view(self):
        a = self.create_article()
        url = reverse('article.views.articles')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.title, resp.content.decode('utf8'))

    def test_article_detail_view(self):
        a = self.create_article()
        url = reverse('article.views.article', args=[a.id])
        resp = self.client.get(url)

        self.assertEqual(url, a.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.title, resp.content.decode('utf8'))

    def test_empty_article(self):
        self.client.login(username='test_user', password='test_pwd') #important

        create_url = reverse('article.views.create')

        resp = self.client.post(create_url, {'title':'   ', 'content': '    '})#if space chars entered
        self.assertEqual(resp.status_code, 200)

    def test_REST_api(self):

        api_url = '/articles/api/article/?format=xml&title__contains=blog'
        resp = self.client.get(api_url)
        self.assertEqual(resp.status_code, 200)

class CommentTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='test_user', email='test@hotmail.com', password='test_pwd')

        self.article = Article.objects.create(title         = "test_article",
                                              content       = "This is content of test_article",
                                              creation_date = timezone.now(),
                                              author        = self.user)
        self.article.save()

        self.client = Client()

    def add_comment(self, content="test comment content"):

        return Comment.objects.create(content       = content,
                                      creation_date = timezone.now(),
                                      article       = self.article,
                                      author        = self.user)

    def test_add_comment(self):

        self.client.login(username='test_user', password='test_pwd') #important
        url = reverse('article.views.add_comment', args=[self.article.id])
        # resp = self.client.get(url)
        #
        # self.assertEqual(resp.status_code, 200)
        # check empty content

        resp = self.client.post(url, {'content': 'this is test comment content'})
        self.assertEqual(resp.status_code, 302)

        comments = self.article.comment_set.all()
        self.assertEqual(comments.count(), 1)

        # check every field of comment
        self.assertEqual(comments[0].article.id, self.article.id)
        self.assertEqual(comments[0].author.username, 'test_user')
        self.assertEqual(comments[0].author.email, 'test@hotmail.com')
        self.assertEqual(comments[0].content, 'this is test comment content')

    def test_empty_comment(self):

        self.client.login(username='test_user', password='test_pwd') #important
        url = reverse('article.views.add_comment', args=[self.article.id])
        resp = self.client.post(url, {'content': '    '})#if space chars entered
        self.assertEqual(resp.status_code, 200)

    def test_comment_view(self):
        c = self.add_comment()
        url = reverse('article.views.article', args=[c.article.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(c.content, resp.content.decode('utf8'))

    def test_comment_model(self):
        c = self.add_comment()
        self.assertTrue(isinstance(c, Comment))

    def test_REST_api(self):

        api_url = '/articles/api/comment/?format=json&content__contains=xxx'
        resp = self.client.get(api_url)
        self.assertEqual(resp.status_code, 200)