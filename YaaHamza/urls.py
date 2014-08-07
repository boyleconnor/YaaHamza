from django.conf.urls import patterns, include, url
from django.contrib import admin
from YaaHamza.views import Home

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dictionary/', include('dictionary.urls', namespace='dictionary')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)