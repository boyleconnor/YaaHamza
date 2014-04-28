from django.conf.urls import patterns, url
from django.contrib import admin
from arabic.views import *
admin.autodiscover()

urlpatterns = patterns('arabic.views',
    url(r'root/(?P<pk>\d+)/$', RootDetail.as_view(), name='root-detail'),
    url(r'word/(?P<pk>\d+)/$', WordDetail.as_view(), name='word-detail'),
    url(r'word/create/$', WordCreate.as_view(), name='word-create'),
    url(r'word/(?P<pk>\d+)/edit/', WordUpdate.as_view(), name='word-update'),
    url(r'word/(?P<pk>\d+)/delete/', WordDelete.as_view()),
    url(r'search/$', Search.as_view(), name='search'),
    url(r'^$', Home.as_view(), name='home'),
)