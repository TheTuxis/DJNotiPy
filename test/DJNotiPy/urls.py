from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'DJNotiPy.views.home', name='home'),
    # url(r'^DJNotiPy/', include('DJNotiPy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(
        r'^$',
        'apps.example.views.view_example_index',
        name='view_example_index'
    ),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^ntf/',
        include(
            'apps.notification.urls',
            namespace='notification',
            app_name='notification'
        )
    ),
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.MEDIA_ROOT,
        }
    ),
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.MEDIA_ROOT,
        }
    ),
)
