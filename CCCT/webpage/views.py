from django.shortcuts import render
from webpage.models import *

# Create your views here.

def home(request):
	return render(request, 'webpage/home.html', )

def member(request):
	context = {'profesors': Member.objects.filter(ctype = 0).order_by('name'), 'auxiliar': Member.objects.filter(ctype = 1).order_by('name')}
	return render(request, 'webpage/member.html', context)

def project(request):
	context = {'projects': Project.objects.all()}
	return render(request, 'webpage/project.html', context)