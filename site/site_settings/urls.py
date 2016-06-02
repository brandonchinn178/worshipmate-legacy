from django.conf.urls import include, url

from main.views import *
from database.views import *

urlpatterns = [
    url(r'^$', DatabaseView.as_view(), name='home'),
    url(r'^song/(?P<slug>.+)/$', SongView.as_view(), name='song'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^admin/', include('admin.urls', namespace='admin')),
]

# just need to pass in context
handler404 = get_handler(404)
handler500 = get_handler(500)
