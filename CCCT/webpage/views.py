from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from webpage.models import *

# Create your views here.

def home(request):
	return render(request, 'webpage/home.html', )

def member(request):
	context = {'profesors': Member.objects.filter(ctype = 0).order_by('name'), 'retired': Member.objects.filter(ctype = 2).order_by('name'), 'colaborator': Member.objects.filter(ctype = 3).order_by('name'), 'auxiliar': Member.objects.filter(ctype = 1).order_by('name')}
	return render(request, 'webpage/member.html', context)

def project(request):
	context = {'projects': Project.objects.all()}
	return render(request, 'webpage/project.html', context)

def subject(request):
	context = {'courses': Course.objects.filter(ctype = 0), 'pcourses': Course.objects.filter(ctype = 1)}
	return render(request, 'webpage/course.html', context)

def tesis(request):
	context = {'done': Tesis.objects.filter(status = 2), 'ongoing': Tesis.objects.filter(status = 1), 'offer': Tesis.objects.filter(status = 0) }
	return render(request, 'webpage/tesis.html', context)

def profile(request, name):
	context = {'p': Member.objects.get(link = name)}
	return render(request, 'webpage/profile.html', context)

def editprofile(request, name):
	context = {'p': Member.objects.get(link = name)}
	return render(request, 'webpage/editprofile.html', context)

def update(request, name):
	p = Member.objects.get(link = name)
	html = request.POST['html']
	p.html = html
	p.save()
	return HttpResponseRedirect(reverse('webpage:profile', args=[p.link], ))