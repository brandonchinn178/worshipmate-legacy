from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'contact.views.index', name='index'),
    url(r'^thanks/', 'contact.views.thanks')
)