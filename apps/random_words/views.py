# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):

	unique_id = get_random_string(length=14)
	context = { "words":unique_id}
	print context
	return render(request, "random_words/index.html", context)

def generate(request):
	return redirect('/random_words/')
