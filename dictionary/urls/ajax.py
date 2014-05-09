from django.conf.urls import patterns, url

urlpatterns = patterns('dictionary.ajax',
    url(r'', 'word_detail', name=''),
)
