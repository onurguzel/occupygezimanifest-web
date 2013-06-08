from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import object_tools
admin.autodiscover()
object_tools.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'occupygezimanifest.views.home', name='home'),
    # url(r'^occupygezimanifest/', include('occupygezimanifest.foo.urls')),
    url(r'^$', include('tweets.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^object-tools/', include(object_tools.tools.urls)),
)
