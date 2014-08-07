from django.conf.urls import patterns, include, url
from dictionary.views import WordDetail, WordCreate, WordUpdate, WordDelete

urlpatterns = patterns('',
    url('word/create/$', WordCreate.as_view(), name='word.create'),
    url('word/(?P<pk>\d+)(/(?P<spelling>.+))?/edit/$', WordUpdate.as_view(), name='word.update'),
    url('word/(?P<pk>\d+)(/(?P<spelling>.+))?/delete/$', WordDelete.as_view(), name='word.delete'),
    url('word/(?P<pk>\d+)(/(?P<spelling>.+))?/$', WordDetail.as_view(), name='word.detail'),
)
