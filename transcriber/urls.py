from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('transcriber.views',
    url(r'^$', 'index'),
    url(r'^transcribe/$', 'transcribe'),
    url(r'^(?P<session_id>\d+)/(?P<user_id>\d+)/(?P<speaker_id>\d+)/(?P<speakersession_id>\d+)/(?P<word_id>\d+)/$', 'transcribe'),
)
