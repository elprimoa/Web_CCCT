from django.conf.urls import patterns, url

from webpage import views

urlpatterns = patterns('', 
		url(r'^update/(?P<name>\w+)$', views.update, name='update'),
		url(r'^member/(?P<name>\w+)/edit/$', views.editprofile, name='editprofile'),
		url(r'^member/(?P<name>\w+)/$', views.profile, name='profile'),
		url(r'^tesis/$', views.tesis, name='tesis'),
		url(r'^subject/$', views.subject, name='subject'),
		url(r'^project/$', views.project, name='project'),
		url(r'^member/$', views.member, name='member'),
		url(r'^$', views.home, name='home'),
	)