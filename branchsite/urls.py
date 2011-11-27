from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^events/list', 'publicity.views.events_list'),
    url(r'^events/detail', 'publicity.views.event_detail'),
    url(r'^$', 'publicity.views.home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
