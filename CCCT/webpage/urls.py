from django.conf.urls import patterns, url

from webpage import views

urlpatterns = patterns('', 
		url(r'^project/$', views.project, name='project'),
		url(r'^member/$', views.member, name='member'),
		url(r'^$', views.home, name='home'),
	)