from django.conf.urls import url
from . import views

urlpatterns = [
	
	url(r'^$', views.map, name='map'),
	url(r'^map/visuals/$', views.map, name='map'),
	url(r'^map/chart/$', views.chart, name='chart')
	
]