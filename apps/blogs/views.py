# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	context = {"email" : "blog@gmail.com", "name" : "Ryan"}
	return render(request, "index.html", context)

def new(request):
	response = "Placeholder to display new form to create a new blog"
	return HttpResponse(response)

def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		print request.POST['blog_name']
		print request.POST['desc']
		request.session['name'] = "test"
		print"*"*50

		return redirect('/blogs')
	else:
		return redirect('/blogs')
def display(request, id):
	response = "placeholder to display blog " + id
	return HttpResponse(response)

def edit(request, id):
	response = "placeholder to edit blog " + id
	return HttpResponse(response)

def delete(request, id):
	response = "placeholder to delete blog " + id
	return HttpResponse(response)		
# Create your views here.
