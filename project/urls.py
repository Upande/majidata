from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from majidata import views
from django.contrib.auth.decorators import login_required
from tastypie.api import Api
from majitables.api import CountyResource,TownResource, SlumResource, AreaResource, WSPResource
from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(CountyResource())
v1_api.register(TownResource())
v1_api.register(SlumResource())
v1_api.register(AreaResource())
v1_api.register(WSPResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^(?:index/?)?$', views.index),
	url(r'^visualize/',  TemplateView.as_view(template_name='map.html'), name="map_page"),
    #url(r'^data/', include('project.maji.urls')),
	url(r'^data/$', views.data_index),
	url(r'^data/tables/(?P<geographic_level>[^/]*)/(?P<category>[^/]*)/(?P<table>[^/]*)/$', views.get_tables),
	url(r'^data/tablenames/(?P<geographic_level>[^/]*)/(?P<category>[^/]*)/$', views.get_table_names),
	url(r'^test/$', login_required(TemplateView.as_view(template_name='test.html')), name="tests_page"),
	url(r'^api/', include(v1_api.urls)),
	url(r'^cols/', views.getcolumns),
	
)
