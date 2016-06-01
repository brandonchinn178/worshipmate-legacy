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
    # login urls
    url(r'^login/$', login, login_kwargs, name='login'),
    url(r'^logout/$', logout, logout_kwargs, name='logout'),
]
