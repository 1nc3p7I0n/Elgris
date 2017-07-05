from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from .models import Distrib

# Create your views here.
def index(request):
	countries = Distrib.objects.order_by().values('country').distinct()
	states = Distrib.objects.order_by().values('state').distinct()
	cities = Distrib.objects.order_by().values('city').distinct()
	return render( request, 'index.html', { 'countries': countries, 'states': states, 'cities': cities }  )

def more_city(request, city_name):
    if request.is_ajax():
	    data = Distrib.objects.order_by('name').filter(city = city_name)
	    data = serializers.serialize('json', data)
	    return HttpResponse(data)

def more_state(request, state_name):
    if request.is_ajax():
	    data = Distrib.objects.order_by('name').filter(state = state_name)
	    data = serializers.serialize('json', data)
	    return HttpResponse(data)

def more_country(request, country_name):
    if request.is_ajax():
	    data = Distrib.objects.order_by('name').filter(country = country_name)
	    data = serializers.serialize('json', data)
	    return HttpResponse(data)
