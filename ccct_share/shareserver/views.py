from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.servers.basehttp import FileWrapper
from shareserver.models import *
import os
import mimetypes

# Create your views here.

def home(request):
	d = Directory.objects.get(id = 1)
	cur_dir = "/"
	added_dir = d.added.split("\n")
	for dr in added_dir:
		if(dr != ""):
			cur_dir = cur_dir + dr + "/"
	dr, f = [], []
	lis = os.listdir(d.base + cur_dir)
	for l in lis:
		if(os.path.isfile(d.base + cur_dir + l)):
			f.append(l)
		else:
			dr.append(l)
	context = {'element': dr, 'file' : f, 'cur': cur_dir}
	return render(request, 'shareserver/base.html', context)

def navigate(request):
	new_dir = request.POST['directory']
	d = Directory.objects.get(id = 1)
	added = d.added.split("\n")
	cur_dir = "/"
	for dr in added:
		if(dr != ""):
			cur_dir = cur_dir + dr + "/"
	if(new_dir == "file"):
		f = request.FILES['file']
		filename = d.base + cur_dir + str(f)
		with open(filename, 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)
	elif(new_dir == ".."):
		d.added = ""
		for i in range(len(added) - 1):
			if(added[i] != ""):
				d.added = d.added + "\n" + added[i]
	else:
		d.added = d.added + "\n" + new_dir
	d.save()
	return HttpResponseRedirect(reverse('shareserver:home', ))

def download(request):
	filename = request.POST['filename']
	d = Directory.objects.get(id = 1)
	added = d.added.split("\n")
	cur_dir = "/"
	for dr in added:
		if(dr != ""):
			cur_dir = cur_dir + dr + "/"
	response_data = d.base + cur_dir + filename
	return HttpResponse(response_data)