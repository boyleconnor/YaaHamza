from django.conf.urls import patterns, url
from django.contrib import admin
from arabic.views import *
from arabic.ajax import *
admin.autodiscover()

urlpatterns = patterns('arabic.views',
    url(r'root/(?P<pk>\d+)/$', RootDetail.as_view(), name='root'),
    url(r'word/(?P<pk>\d+)/$', WordDetail.as_view(), name='word'),
    url(r'search/$', Search.as_view(), name='search'),
    url(r'^$', Home.as_view(), name='home'),
)