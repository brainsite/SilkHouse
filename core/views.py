# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .form import MailForm, CallForm, ReviewForm
from shop.models import Scarf

# Create your views here.


def landing(request):
    scarfs = Scarf.objects.on_sale()
    scarfs_count = scarfs.count()
    scarfs = scarfs[:8]

    mail_form = MailForm(prefix='mail')
    call_form = CallForm(prefix='call')
    review_form = ReviewForm(prefix='review')
    mail_form_errors = None
    call_form_errors = None
    review_form_errors = None

    if request.method == 'POST' and 'mail' in request.POST:
        mail_form = MailForm(request.POST, prefix='mail')
        if mail_form.is_valid():
            messages.success(request, "Mail Form Success!")
            return redirect('home')
        else:
            messages.error(request, 'Mail Form Error')

    if request.method == 'POST' and 'call' in request.POST:
        call_form = CallForm(request.POST, prefix='call')
        if call_form.is_valid():
            messages.success(request, "Call Form Success!")
            return redirect('home')
        else:
            print(call_form.errors)
            messages.error(request, 'Call Form Error')

    if request.method == 'POST' and 'review' in request.POST:
        review_form = ReviewForm(request.POST, prefix='call')
        if review_form.is_valid():
            messages.success(request, "Review Form Success!")
            return redirect('home')
        else:
            print(call_form.errors)
            messages.error(request, 'Review Form Error')

    mail_form.helper.form_action = reverse('contact')
    call_form.helper.form_action = reverse('contact')
    review_form.helper.form_action = reverse('contact')

    #
    # Sessions
    #

    context = {'landing': True,
               #
               'mail_form': mail_form,
               'call_form': call_form,
               'review_form': review_form,
               'mail_form_errors': mail_form_errors,
               'call_form_errors': call_form_errors,
               'review_form_errors': review_form_errors,
               #
               'scarfs': scarfs,
               'scarfs_count': scarfs_count,
               #
               'basket': request.session.get('basket', True),
               'favorites': request.session.get('favorites'),
               }
    return render(request, 'landing/base.html', context)

