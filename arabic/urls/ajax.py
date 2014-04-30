from django.conf.urls import patterns, url

urlpatterns = patterns('arabic.ajax',
    url(r'', 'word_detail', name=''),
)
