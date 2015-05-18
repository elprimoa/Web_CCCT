from django.conf.urls import patterns, url

from shareserver import views

urlpatterns = patterns('', 
		url(r'^$', views.home, name='home'),
		url(r'^navigate/$', views.navigate, name='navigate'),
		url(r'^download/$', views.download, name='download'),
	)