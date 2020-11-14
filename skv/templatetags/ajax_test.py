# -*- coding: utf-8 -*-
from django import template

register = template.Library()


@register.simple_tag
def btn():
    btn = """
            <button id="favorite" data-test="test_data" class="btn btn-primary" type="button">
                <span class="glyphicon glyphicon-thumbs-up"></span> Like
            </button>"""
    return btn