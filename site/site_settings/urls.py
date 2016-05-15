from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render

from main.views import *
from database.views import *

admin.autodiscover()

urlpatterns = [
    url(r'^$', DatabaseView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^database/(?P<title>[\w\W]+)/$', SongView.as_view(), name='song'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^transpose/$', TransposeView.as_view(), name='transpose'),
]

# just need to pass in context
handler404 = lambda request: render(request, '404.html', {'title': 'Page Not Found'})
handler500 = lambda request: render(request, '500.html', {'title': 'Server Error'})