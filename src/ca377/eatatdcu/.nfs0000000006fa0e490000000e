from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Restaurant,Campus
import json
import requests


def index(request):
    template = loader.get_template('eatatdcu/index.html')
    return HttpResponse(template.render({},request))

def restaurants(request):
    template = loader.get_template('eatatdcu/restaurants.html')
    campus_name = request.GET.get('campus','').lower()
    try:
        campus = Campus.objects.get(name=campus_name)
        restaurants = Restaurant.objects.filter(campus_id=campus,is_restaurant=True)
        cafes = Restaurant.objects.filter(campus_id=campus,is_restaurant=False)
    except Restaurant.DoesNotExist:
        return HttpResponse(template.render({'error':'No such restaurant'},request))
    except Campus.DoesNotExist:
        return HttpResponse(template.render({'error':'No such campus'},request))
    return HttpResponse(template.render({'restaurants':restaurants,'cafes':cafes},request))

def specials(request,restaurant):
    template = loader.get_template('eatatdcu/specials.html')
    #restaurant = request.GET.get('restaurant','')
    #specials_url = "http://jfoster.pythonanywhere.com/specials/" + restaurant
    #specials_info = requests.get(specials_url)
    #jason = specials_info.json()
    #r = jason["date"]

    specials_url = requests.get("http://jfoster.pythonanywhere.com/specials/" + restaurant)
    rest = specials_url.json()
    return HttpResponse(template.render(rest,request))

