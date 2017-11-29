#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 16:09
# @Author  : huanghe
# @Site    : 
# @File    : blog_tags.py
# @Software: PyCharm
from django import template
from  ..models import Post,Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()
