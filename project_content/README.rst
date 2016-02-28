=======================
simple blog application
=======================

This is a simple Django app for testing candidates' django skills.

Quick start
-----------

1. Add "article" and "account" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'article',
	'account',
	'bootstrap_toolkit'
    ]

2. Set urls.py in your project like this::

    
	urlpatterns = [

	    url(r'^$', 'article.views.articles'),
	    url(r'^admin/', include(admin.site.urls)),
	    url(r'^articles/', include('article.urls')),
	    url(r'^accounts/', include('account.urls')),
	]

3. To create the models, run as follows

	python manage.py makemigrations
	python manage.py migrate

4. Start the development server and visit http://127.0.0.1:8000/

