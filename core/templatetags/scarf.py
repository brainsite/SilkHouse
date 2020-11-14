# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

from shop.models import Scarf
from colors16.models import Colors

register = template.Library()


@register.inclusion_tag('shop/extra/thumbnail.html')
def scarf_thumbnail(pk):
    scarf = Scarf.objects.get(pk=pk)
    return {'scarf': scarf, }


@register.inclusion_tag('shop/extra/color_row.html')
def color_row(pk):
    color = Colors.objects.get(pk=pk)
    scarfs = Scarf.objects.filter(l_color=color.id)
    return {'color': color, 'scarfs': scarfs, }

#
# @register.simple_tag()
# def favorite_btn(pk=False):
#     flag = """<i class="fa fa-star-o"></i>"""
#     if pk:
#             flag = """<i class="fa fa-star"></i>"""
#     btn = """<div id="favorite_div"><span id="favorite" data-pk="{}" class="h1">{}</span></div>""".format(pk, flag)
#     return btn

@register.simple_tag
def active_page(request, view_name):
    from django.core.urlresolvers import resolve, Resolver404
    if not request:
        return ""
    try:
        return "active" if resolve(request.path_info).url_name == view_name else ""
    except Resolver404:
        return ""


@register.filter
def get_item(dictionary, key):
    print(dictionary)
    print(key)
    key = str(key)
    return dictionary[key]