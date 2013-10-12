from tastypie.resources import ModelResource
from tastypie.authorization import Authorization,DjangoAuthorization, ReadOnlyAuthorization
from tastypie.constants import ALL
from models import *

class CountyResource(ModelResource):
	class Meta:
		queryset = Summaryshtcounty.objects.all()
		resource_name = 'county'
		authorization= ReadOnlyAuthorization()
		filtering = {}
		for f in Summaryshtcounty._meta.fields:
			filtering.update({f.name : ALL})
		
class TownResource(ModelResource):
	class Meta:
		queryset = Summaryshttown.objects.all()
		resource_name = 'town'
		authorization= ReadOnlyAuthorization()
		filtering = {}
		for f in Summaryshttown._meta.fields:
			filtering.update({f.name : ALL})
		
class SlumResource(ModelResource):
	class Meta:
		queryset = Summaryshtslum.objects.all()
		resource_name = 'slum'
		authorization= ReadOnlyAuthorization()
		filtering = {}
		for f in Summaryshtslum._meta.fields:
			filtering.update({f.name : ALL})
	
class AreaResource(ModelResource):
	class Meta:
		queryset = Areasummarysheet.objects.all()
		resource_name = 'area'	
		authorization= ReadOnlyAuthorization()
		filtering = {}
		for f in Areasummarysheet._meta.fields:
			filtering.update({f.name : ALL})
		
class WSPResource(ModelResource):
	class Meta:
		queryset = Summaryshtwsp.objects.all()
		resource_name = 'wsp'
		authorization= ReadOnlyAuthorization()
		filtering = {}
		for f in Summaryshtwsp._meta.fields:
			filtering.update({f.name : ALL})