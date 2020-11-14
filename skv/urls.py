# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.views.generic import TemplateView



urlpatterns = patterns('skv.views',
    url(r'^/$', 'index', name='index'),
    url(r'^demo/$', 'demo', name='demo'),
    url(r'^contacts/$', 'contacts', name='contacts'),

    url(r'^spirit8/original$', TemplateView.as_view(template_name='demo/spirit8.html'), name='spirit8'),

    # AJAX
    url(r'^ajax/$', TemplateView.as_view(template_name='skv/ajax_test.html'), name='ajax'),
    url(r'^ajax/test$', 'ajax_test', name='ajax_test'),
    
    # Old silk demo
    url(r'^silk/$', 'silk_old_demo_index', name='silk_index'),
    url(r'^silk/about/$', 'silk_old_demo_about', name='silk_about'),
    url(r'^silk/care/$', 'silk_old_demo_care', name='silk_care'),
    url(r'^silk/delivery/$', 'silk_old_demo_delivery', name='silk_delivery'),
    url(r'^silk/contacts/$', 'silk_old_demo_contacts', name='silk_contacts'),
)

