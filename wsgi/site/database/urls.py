from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'database.views.index', name='index'),
    url(r'^(?P<title>[\w\W]+)/$', 'database.views.detail', name='detail')
)