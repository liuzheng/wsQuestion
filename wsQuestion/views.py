#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2014
# Gmail:liuzheng712
#

from django.http import HttpResponse
from django.shortcuts import render_to_response
def index(request):
    return render_to_response('index.html')
