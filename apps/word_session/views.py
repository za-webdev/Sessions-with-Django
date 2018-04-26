# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from time import localtime,strftime
from django.contrib import messages

def index(request):
	# if 'words' not in request.session:
	# 	request.session['words']=[]
	return render(request,'word_session/session.html')

def process(request):
	
	context={
		'date':strftime("%b %d %Y",localtime()),
		'time':strftime(" %I:%M %p",localtime()),
		'word':request.POST['word'],
		'color':request.POST['color']
		# 'font': request.POST['font']
		}

	if 'info' not in request.session:
		request.session['info']=[context]
	
	else:
		request.session['info'].append(context)
	request.session.modified=True
	return redirect("/")
	
def clear(request):
	request.session.clear()
	return redirect('/')