from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('arabic.views',
    # Examples:
    # url(r'^$', 'YaaHamza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'root/(?P<pk>\d+)/$', 'root', name='root'),
    url(r'word/(?P<pk>\d+)/$', 'word', name='word'),
    url(r'search/(?P<q>.*)/$', 'search', name='get_search'),
    url(r'search/$', 'search', name='post_search'),
    url(r'^$', 'home', name='home'),
)