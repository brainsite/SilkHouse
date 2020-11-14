from django.conf.urls import patterns, url, include

urlpatterns = patterns('shop.views',
    url(r'^colors/$', 'colors_filter', name='colors'),

    url(r'^$', 'catalog', name='home'),
    url(r'^catalog/$', 'catalog', name='catalog'),
    url(r'^catalog/(?P<page>\d+)/$', 'catalog', name='catalog_page'),
    url(r'^catalog/color/$', 'colors_filter', name='catalog_color'),
    url(r'^filter/(?P<f_name>[-\w\d]+)/$', 'catalog', name='filter'),
    #
    url(r'^product/(?P<pk>\d+)/$', 'product', name='product'),
    url(r'^product/(?P<pk>\d+)/img/$', 'product_img', name='product_img'),
    #
    url(r'^basket/$', 'basket', name='basket'),
    # url(r'^product/(?P<pk>\d+)/edit/$', 'edit', name='product_edit'),
    #
    # Ajax
    #
    url(r'^ajax/menu/$', 'ajax_menu', name='ajax_menu'),
    # Favorite Button
    url(r'^ajax/favorite/(?P<pk>\d+)/$', 'ajax_favorite', name='favorite'),
    # Favorites ROW
    url(r'^ajax/favorites/$', 'ajax_favorites', name='ajax_favorites'),
    # Basket
    url(r'^basket/add/(?P<pk>\d+)/$', 'basket_add', name='basket_add'),
    url(r'^basket/remove/(?P<pk>\d+)/$', 'basket_remove', name='basket_remove'),
    url(r'^basket/drop/(?P<pk>\d+)/$', 'basket_drop', name='basket_drop'),


)
