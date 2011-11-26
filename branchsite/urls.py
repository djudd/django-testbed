from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'branchsite.views.home', name='home'),
    # url(r'^branchsite/', include('branchsite.foo.urls')),

    #url(r'^schedule/', include('schedule.urls')),

    url(r'^events/list', 'publicity.views.events_list'),
    url(r'^home', 'publicity.views.home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
