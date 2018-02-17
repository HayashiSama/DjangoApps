# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	response = "placeholder to display a new form to create a new blog"
	return HttpResponse(response)
# Create your views here.
