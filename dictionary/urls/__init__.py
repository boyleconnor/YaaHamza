from django.conf.urls import patterns, url, include
from django.contrib import admin
from dictionary.views import *
admin.autodiscover()

urlpatterns = patterns('dictionary.views',
    url(r'^root/', include('dictionary.urls.root')),
    url(r'^word/', include('dictionary.urls.word')),
    url(r'^search/$', WordSearch.as_view(), name='search'),
    url(r'^$', Home.as_view(), name='home'),
)