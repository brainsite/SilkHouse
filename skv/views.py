# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse

from .form import MailForm, CallForm, ReviewForm
# Create your views here.

def index(request):
    context = {}
    return render(request, 'skv/index.html', context)

def demo(request):
    context = {}
    return render(request, 'skv/demo.html', context)

def contacts(request):
    mail_form = MailForm(prefix='mail')
    call_form = CallForm(prefix='call')
    mail_form_errors = None
    call_form_errors = None

    if request.method == 'POST' and 'mail' in request.POST:
        mail_form = MailForm(request.POST, prefix='mail')
        if mail_form.is_valid():
            messages.success(request, "Mail Form Success!")
            return redirect('skv:contacts')
        else:
            messages.error(request, 'Mail Form Error')

    if request.method == 'POST' and 'call' in request.POST:
        call_form = CallForm(request.POST, prefix='call')
        if call_form.is_valid():
            messages.success(request, "Call Form Success!")
            return redirect('skv:contacts')
        else:
            print(call_form.errors)
            messages.error(request, 'Call Form Error')

    context = {'mail_form': mail_form,
               'call_form': call_form,
               'mail_form_errors': mail_form_errors,
               'call_form_errors': call_form_errors,
               }
    return render(request, 'skv/contacts.html', context)

#
# Ajax test
#

def ajax_test(request):
    pass
    return HttpResponse('Test AJAX')

#
#
#
# Old silk demo
#
#
#

def silk_old_demo_index(request):
    context = {'msg': 'Hello Amigo!'
               }
    return render(request, 'silk/index.html', context)

def silk_old_demo_about(request):
    context = {'msg': 'Hello Amigo!'
               }
    return render(request, 'silk/about.html', context)

def silk_old_demo_care(request):
    context = {'msg': 'Hello Amigo!'
               }
    return render(request, 'silk/care.html', context)

def silk_old_demo_delivery(request):
    context = {'msg': 'Hello Amigo!'
               }
    return render(request, 'silk/delivery.html', context)

def silk_old_demo_contacts(request):
    mail_form = MailForm(prefix='mail')
    call_form = CallForm(prefix='call')
    mail_form_errors = None
    call_form_errors = None

    if request.method == 'POST' and 'mail' in request.POST:
        mail_form = MailForm(request.POST, prefix='mail')
        if mail_form.is_valid():
            return redirect('home')

    if request.method == 'POST' and 'call' in request.POST:
        call_form = CallForm(request.POST, prefix='call')
        if call_form.is_valid():
            return redirect('home')

    context = {'mail_form': mail_form,
               'call_form': call_form,
               'mail_form_errors': mail_form_errors,
               'call_form_errors': call_form_errors,
               }
    return render(request, 'silk/contacts.html', context)

