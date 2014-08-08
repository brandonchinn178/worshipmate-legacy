from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worshipdatabase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^database/', include('database.urls', namespace='database')),
    url(r'^about/$', 'main.views.about', name='about'),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^transpose/', include('transpose.urls', namespace='transpose')),
)
