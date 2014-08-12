from django.conf.urls import patterns, include, url
from dictionary.views import WordDetail, DeriverDetail, Search

urlpatterns = patterns('',
    url('word/search/$', Search.as_view(), name='word.search'),
    url('word/(?P<pk>\d+)/(?P<spelling>.+)/$', WordDetail.as_view(), name='word.detail'),
    url('pattern/(?P<pk>\d+)/(?P<name>.+)/$', DeriverDetail.as_view(), name='pattern.detail'),
)