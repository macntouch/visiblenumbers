from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from backend.views import ShowNumbers

urlpatterns = patterns('',
                       # Examples:
                       url(r'^aastra$',ShowNumbers.as_view() ),
                       # url(r'^visiblenumbers/', include('visiblenumbers.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
)