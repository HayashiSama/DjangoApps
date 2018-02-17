# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
	if "count" not in request.session:
		request.session['count']=0
		return redirect('/random_words/generate')

	else:
		context = { "words": request.session['word'], "count" : request.session['count']}
		return render(request, "random_words/index.html", context)

def generate(request):
	request.session['count'] +=1
	request.session['word']= get_random_string(length=14)
	
	return redirect('/random_words/')
