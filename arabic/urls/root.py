from django.conf.urls import patterns, url
from arabic.views import RootDetail

urlpatterns = patterns('arabic.views',
    url('(?P<pk>\d+)/$', RootDetail.as_view(), name='root-detail'),
)
