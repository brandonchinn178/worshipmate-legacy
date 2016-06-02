from django.conf.urls import url
from django.contrib.auth.views import login, logout

from admin.views import *

login_kwargs = {
    'template_name': 'admin/login.html',
}

logout_kwargs = {
    'next_page': 'login',
}

urlpatterns = [
    url(r'^$', MainView.as_view(), name='index'),
    url(r'^add-song/$', AddSongView.as_view(), name='add_song'),
    url(r'^edit-song/(?P<slug>.+)/$', EditSongView.as_view(), name='edit_song'),
    url(r'^themes/$', ThemesView.as_view(), name='themes'),
    url(r'^account/$', AccountView.as_view(), name='account'),
    # login urls
    url(r'^login/$', login, login_kwargs, name='login'),
    url(r'^logout/$', logout, logout_kwargs, name='logout'),
]
