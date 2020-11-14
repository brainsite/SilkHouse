# -*- coding: utf-8 -*-

from django import forms
from django.core.urlresolvers import reverse

from localflavor.us.forms import USPhoneNumberField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Field
from crispy_forms.bootstrap import StrictButton, PrependedText


class MailForm(forms.Form):
    name = forms.CharField(
        label=u'Имя',
        max_length=128,
    )

    mail = forms.EmailField(
        label=u'Mail',
        min_length=5,
        max_length=256,
    )

    text = forms.CharField(
        label=u'Вопрос',
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(MailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-mailForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('skv:contacts')
        self.helper.form_show_labels = False

        # self.helper.add_input(Submit('submit', 'Отправить'))

        self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-12'
        self.helper.layout = Layout(
            # 'name',
            PrependedText('name', '<span class="glyphicon glyphicon-user"></span>', placeholder=u'Имя'),
            # 'mail',
            PrependedText('mail', '@', placeholder=u'Ваш адрес'),
            # 'text',
            Field('text', rows="2", placeholder=u'Напишите ваш вопрос в это поле.'),
            Div(Div(StrictButton(u'Отправить', type='submit', css_class='btn-default', name='mail'),
                    css_class="text-center"),
                css_class="form-group")
        )


class CallForm(forms.Form):
    name = forms.CharField(
        label=u'Имя',
        max_length=128,
    )

    phone = USPhoneNumberField(
        label=u'Телефон',
        error_messages={'invalid': u'Необходимо ввести девятизначный номер.'}
    )

    def __init__(self, *args, **kwargs):
        super(CallForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-callForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('skv:contacts')
        # self.helper.form_error_title = 'Form Errors'
        # self.helper.form_show_errors = True
        self.helper.form_show_labels = False

        # self.helper.add_input(Submit('submit', u'Отправить'))

        self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-12'
        self.helper.layout = Layout(
            # 'name',
            PrependedText(u'name', '<span class="glyphicon glyphicon-user"></span>', placeholder=u'Имя'),
            # 'phone',
            PrependedText(u'phone', '<span class="glyphicon glyphicon-phone"></span>', placeholder=u'xxx xxx-xxxx'),
            Div(Div(StrictButton(u'Отправить', type='submit', css_class='btn-default', name='call'),
                    css_class="text-center"),
                css_class="form-group")
        )


class ReviewForm(forms.Form):
    name = forms.CharField(
        label=u'Имя',
        max_length=128,
    )

    text = forms.CharField(
        label=u'Вопрос',
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-reviewForm'
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('skv:contacts')
        self.helper.form_show_labels = False

        self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-12'
        self.helper.layout = Layout(
            # 'name',
            PrependedText('name', '<span class="glyphicon glyphicon-user"></span>', placeholder=u'Имя'),
            # 'text',
            Field('text', rows="2", placeholder=u'Напишите ваш отзыв в это поле.'),
            Div(Div(StrictButton(u'Отправить отзыв', type='submit', css_class='btn-default', name='review'),
                    css_class="text-center"),
                css_class="form-group")
        )



