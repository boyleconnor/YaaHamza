from django.conf.urls import patterns, url
from dictionary.ajax import root_detail, root_list
from dictionary.views import RootDetail, RootCreate, RootUpdate, RootDelete

urlpatterns = patterns('dictionary.views',
    url(r'(?P<pk>\d+)/$', RootDetail.as_view(), name='root-detail'),
    url(r'create/$', RootCreate.as_view(), name='root-create'),
    url(r'(?P<pk>\d+)/edit/$', RootUpdate.as_view(), name='root-update'),
    url(r'(?P<pk>\d+)/delete/$', RootDelete.as_view(), name='root-delete'),
    url(r'ajax_detail/$', root_detail, name='root-detail-json'),
    url(r'ajax_list/$', root_list, name='root-list-json'),
)
