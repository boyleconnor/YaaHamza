from django.conf.urls import url, patterns
from dictionary.views import WordDetail, WordUpdate, WordDelete, WordCreate

urlpatterns = patterns('dictionary.views',
    url(r'(?P<pk>\d+)/$', WordDetail.as_view(), name='word-detail'),
    url(r'create/$', WordCreate.as_view(), name='word-create'),
    url(r'(?P<pk>\d+)/edit/$', WordUpdate.as_view(), name='word-update'),
    url(r'(?P<pk>\d+)/delete/$', WordDelete.as_view(), name='word-delete'),
)

