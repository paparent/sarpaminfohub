from django.conf.urls.defaults import patterns, include
from django.conf.urls.defaults import handler500, handler404 #@UnusedImport

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sarpaminfohub/', include('sarpaminfohub.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

urlpatterns = patterns('',
    (r'', include('sarpaminfohub.infohub.urls')),
)