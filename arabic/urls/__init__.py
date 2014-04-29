from django.conf.urls import patterns, url, include
from django.contrib import admin
from arabic.views import *
admin.autodiscover()

urlpatterns = patterns('arabic.views',
    url(r'^root/', include('arabic.urls.root')),
    url(r'^word/', include('arabic.urls.word')),
    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^$', Home.as_view(), name='home'),
)