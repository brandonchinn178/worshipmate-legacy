from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import *
from database.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worshipdatabase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^database/$', DatabaseView.as_view(), name='database'),
    url(r'^database/(?P<title>[\w\W]+)/$', SongView.as_view(), name='song'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^transpose/', TransposeView.as_view(), name='transpose'),
)
