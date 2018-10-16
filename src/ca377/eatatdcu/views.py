from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from django.core.exceptions import ObjectDoesNotExist
from eatatdcu.models import Campus, Restaurant
def index(request):
	template = loader.get_template('eatatdcu/index.html')
	return HttpResponse(template.render({},request))

def restaurants(request):
	template = loader.get_template('eatatdcu/restaurants.html')
	try:
		campus = request.GET.get('campus').lower()
		campusdata = Campus.objects.filter(name = campus)
		#if campus  == 'glasnevin':
		#	campusdata = 1
		#elif campus == 'st pats':
		#	campusdata = 2
		#elif campus  == 'dcu alpha':
		#	campusdata = 3
		#elif campus == 'all hallows':
		#	campusdata = 4


		resdata = Restaurant.objects.filter(campus_id = campusdata)
		return HttpResponse(template.render({'campus': campus, 'resdata': resdata},request))
	except Campus.DoesNotExist:
		return HttpResponse('No such campus') 
	
  