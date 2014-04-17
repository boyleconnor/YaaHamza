from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'YaaHamza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^arabic/', include('arabic.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
