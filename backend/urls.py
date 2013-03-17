from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from backend.views import ShowNumbers, StreamAudioNumbers

urlpatterns = patterns('',
    url(r'^aastra$',ShowNumbers.as_view() ),
    url(r'^aastra/audio$',StreamAudioNumbers.as_view() ),
)