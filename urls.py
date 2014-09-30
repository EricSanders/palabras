from django.conf.urls.defaults import patterns, include, url
from palabras.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main_page),

    # Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),

    # Sites
    url(r'^transcriber/', include('transcriber.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
