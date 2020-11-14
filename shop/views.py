# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, render_to_response
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Scarf
from colors16.models import Colors

# Create your views here.

# TODO убрать сессии из контекста, возможно не стоит так как меню не обновляеться через ajax
# TODO favorite_row REWRITE
# TODO edit basket_row_btn, basket_product_btn
# TODO product_info_pannel REWRITE переместить favorite_btn в pannel_header изменить дизайн
# TODO ajax_basket_add проверять что есть в наличии


def catalog(request, f_name=None, page=1):
    tittle = False
    subtittle = False
    if f_name == 'male':
        tittle = "Мужские цвета"
        scarfs = Scarf.objects.on_sale_male()
    elif f_name == 'bicolor':
        scarfs = Scarf.objects.on_sale_bicolor()
        tittle = "Двухцветные платки"
        subtittle = "всего {} расцветки".format(scarfs.count())
    elif f_name == 'multicolor':
        scarfs = Scarf.objects.on_sale_multicolor()
        tittle = "Многоцветные платки"
        subtittle = "всего {} расцветки".format(scarfs.count())
    elif f_name == 'Легкий платок':
        tittle = "Мужские цвета"
        subtittle = "легче 40 грамм"
        scarfs = Scarf.objects.on_sale_lite()
    elif f_name == 'hard':
        tittle = "Плотный платок"
        subtittle = "тяжелее 40 грамм"
        scarfs = Scarf.objects.on_sale_hard()
    else:
        scarfs = Scarf.objects.on_sale()
        tittle = "Каталог"
        subtittle = "все {}".format(scarfs.count())
    #
    # https://docs.djangoproject.com/en/1.8/topics/pagination/
    #
    paginator = Paginator(scarfs, 36)
    try:
        scarfs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        scarfs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        scarfs = paginator.page(paginator.num_pages)
    #

    context = {
        'tittle': tittle,
        'subtittle': subtittle,
        'basket': request.session.get('basket'),
        #
        'scarfs': scarfs,
        'favorites': request.session.get('favorites'),
    }
    return render(request, 'shop/index.html', context)


def product(request, pk):
    scarf = get_object_or_404(Scarf, pk=int(pk))
    #
    basket = request.session.get('basket')
    #
    in_basket = False
    profile = request.session.get(pk)
    if profile:
        in_basket = profile.get('basket')
    #
    favorites = request.session.get('favorites')
    favorite = False
    if favorites:
        if scarf.id in favorites:
            favorite = True
    #
    request.session.modified = True
    context = {
        'scarf': scarf,
        'in_basket': in_basket,
        # Для кнопки
        'favorite': favorite,
        #
        'basket': request.session.get('basket'),
        'favorites': favorites,
    }
    # return render(request, 'shop/scarf_bg.html', context)
    return render(request, 'shop/scarf.html', context)


def product_img(request, pk):
    scarf = get_object_or_404(Scarf, pk=int(pk))
    context = {'scarf': scarf, }
    return render(request, 'shop/big_picture.html', context)


def basket(request):
    """ Вызывает страницу и вставляет basket_div

    rows:
        scarf_thumbnail
        in_basket + basket_btn
        price
        subsumm
    """
    basket = request.session.get('basket')

    scarfs = Scarf.objects.filter(pk__in=basket.keys())

    request.session.modified = True
    context = {
        'scarfs': scarfs,
        #
        'basket': basket,
        'favorites': request.session.get('favorites'),
    }
    return render(request, 'shop/basket.html', context)


def colors_filter(request):
    colors_list = []
    colors = Colors.objects.all()
    for color in colors:
        scarfs = Scarf.objects.completed()
        if scarfs.filter(l_color=color.id).count() > 0:
            colors_list.append(color.id)

    request.session.modified = True
    context = {
        'colors': colors,
        'colors_list': colors_list,
        #
        'basket': request.session.get('basket'),
        'favorites': request.session.get('favorites'),
        }
    return render(request, 'shop/colors.html', context)


# AJAX


def ajax_favorite(request, pk):
    """
    id в сессии это словарь для продукта или профиль
    Смотрим в профиле favorite
    Инвертируем полученое значение
    """
    # Если нет создаем ключ
    # Выставляем флаг в профиле
    favorite = True
    if not request.session.get(pk):
        request.session[pk] = {'favorite': favorite}
    else:
        profile = request.session[pk]
        # Если есть pk
        if profile.get('favorite'):
            # Удаляем ключ favorite если есть
            profile.pop('favorite')
            favorite = False
        else:
            profile['favorite'] = favorite
        request.session[pk] = profile

    # favorites
    scarfs = Scarf.objects.on_sale()
    favorites = []
    for s in scarfs:
        p = request.session.get(str(s.id))
        if p:
            f = p.get('favorite')
            if f:
                favorites.append(s.id)
    request.session['favorites'] = favorites

    request.session.modified = True
    context = {
        'scarf': Scarf.objects.get(pk=pk),
        'favorite': favorite,
        'favorites': favorites,
    }
    return render_to_response('shop/include/favorite_btn.html', context)

# Возвращает basket_div


def ajax_basket(request):
    #
    request.session.modified = True
    context = {
        # 'scarf': Scarf.objects.get(pk=pk),
        # 'in_basket': in_basket,
        # 'basket': basket,
        # 'basket': basket,
        #
        'favorites': request.session.get('favorites'),
    }
    return render_to_response('shop/include/basket_btn_product.html', context)

# Возвращает basket_btn_product

def basket_add(request, pk):
    in_basket = False
    # Если профиля небыло
    if not request.session.get(pk):
        request.session[pk] = {'basket': 1}
        in_basket = 1
    else:
        profile = request.session[pk]
        # Если есть pk
        if profile.get('basket'):
            # Удаляем ключ favorite если есть
            basket = profile.pop('basket')
            profile['basket'] = basket + 1
        else:
            profile['basket'] = 1
        in_basket = profile['basket']
        request.session[pk] = profile
    # basket
    scarfs = Scarf.objects.on_sale()
    basket = {}
    for s in scarfs:
        p = request.session.get(str(s.id))
        if p:
            b = p.get('basket')
            if b:
                basket[s.id] = b
    request.session['basket'] = basket
    #
    request.session.modified = True
    context = {
        'scarf': Scarf.objects.get(pk=pk),
        'in_basket': in_basket,
        'basket': basket,
        # 'basket': basket,
        #
        'favorites': request.session.get('favorites'),
    }
    return render_to_response('shop/include/basket_btn_product.html', context)


def basket_remove(request, pk):
    in_basket = False
    # Если есть профиль
    if request.session.get(pk):
        profile = request.session[pk]
        # Если есть pk
        if profile.get('basket'):
            # Удаляем ключ favorite если есть
            basket = profile.pop('basket')
            if basket > 1:
                profile['basket'] = basket - 1
                in_basket = profile['basket']
        request.session[pk] = profile
    # basket
    scarfs = Scarf.objects.on_sale()
    basket = {}
    for s in scarfs:
        p = request.session.get(str(s.id))
        if p:
            b = p.get('basket')
            if b:
                basket[s.id] = b
    request.session['basket'] = basket
    #
    request.session.modified = True
    context = {
        'scarf': Scarf.objects.get(pk=pk),
        'in_basket': in_basket,
        'basket': basket,
        #
        'favorites': request.session.get('favorites'),
    }
    return render_to_response('shop/include/basket_btn_product.html', context)


def basket_drop(request, pk):
    in_basket = False
    # Если есть профиль
    if request.session.get(pk):
        profile = request.session[pk]
        # Если есть pk
        if profile.get('basket'):
            # Удаляем ключ basket если есть
            profile.pop('basket')
        request.session[pk] = profile
    # basket
    scarfs = Scarf.objects.on_sale()
    basket = {}
    for s in scarfs:
        p = request.session.get(str(s.id))
        if p:
            b = p.get('basket')
            if b:
                basket[s.id] = b
    request.session['basket'] = basket
    #
    request.session.modified = True
    context = {
        'scarf': Scarf.objects.get(pk=pk),
        'in_basket': in_basket,
        'basket': basket,
        #
        'favorites': request.session.get('favorites'),
    }
    return render_to_response('shop/include/basket_btn_product.html', context)

# AJAX session only


def ajax_menu(request):
    context = {
        #
        'basket': request.session.get('basket'),
        'favorites': request.session.get('favorites'),
        }
    return render_to_response('shop/include/base_menu.html', context)


def ajax_favorites(request):
    context = {
        #
        'basket': request.session.get('basket'),
        'favorites': request.session.get('favorites'),
        }
    return render_to_response('shop/include/favorite_div.html', context)
