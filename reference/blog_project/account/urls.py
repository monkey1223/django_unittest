from django.conf.urls import url, include

urlpatterns = [

    url(r'^login/$', 'account.views.login'),
    url(r'^auth/$', 'account.views.auth_view'),
    url(r'^logout/$', 'account.views.logout'),
    url(r'^loggedin/$', 'account.views.loggedin'),
    url(r'^invalid/$', 'account.views.invalid_login'),

    url(r'^register/$', 'account.views.register_user'),
    url(r'^register_success/$', 'account.views.register_success'),
]
