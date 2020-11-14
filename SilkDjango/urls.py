# -*- coding: utf-8 -*-

from django.conf import settings


# TODO Добавить переменные из settings в templates
"""

"""


from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Core
    url(r'^$', 'core.views.landing', name='home'),
    url(r'^#tf-about$', 'core.views.landing', name='about'),
    url(r'^#tf-catalog$', 'core.views.landing', name='catalog'),
    url(r'^#tf-care$', 'core.views.landing', name='care'),
    url(r'^#tf-delivery$', 'core.views.landing', name='delivery'),
    url(r'^#tf-reviews$$', 'core.views.landing', name='reviews'),
    url(r'^#tf-contact$$', 'core.views.landing', name='contact'),

    url(r'^shop/', include('shop.urls', namespace='shop')),

    # SKV
    url(r'^skv/$', 'skv.views.index', name='skv'),
    url(r'^skv/', include('skv.urls', namespace='skv')),
    )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

if settings.DEV:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )