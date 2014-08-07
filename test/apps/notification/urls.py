from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    url(
        r'^get_all/$',
        'apps.notification.views.get_all', name='get_all'
    ),
    url(
        r'^get_new/$',
        'apps.notification.views.get_new', name='get_new'
    ),
    url(
        r'^readed/(?P<id_ntf>\d+)/$',
        'apps.notification.views.readed', name='readed'
    ),
)
