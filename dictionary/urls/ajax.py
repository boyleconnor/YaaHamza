from django.conf.urls import patterns, url
from dictionary.ajax import word_detail

urlpatterns = patterns('dictionary.ajax',
    url(r'word/(?P<pk>/$)', word_detail, name='word-detail-json'),
)
