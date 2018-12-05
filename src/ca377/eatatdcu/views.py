from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Restaurant,Campus
import json,requests

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
    webservice_url = 'http://jfoster.pythonanywhere.com/specials/'+restaurant
    real_time_info = requests.get(webservice_url).json()
    if 'error_msg' in real_time_info:
       return HttpResponse(template.render({'error':real_time_info['error_msg']},request))
    else:
       return HttpResponse(template.render(real_time_info,request))
def contact(request):
    return render(request, 'eatatdcu/contact.html',{})

def explore(request):
    return render(request, 'eatatdcu/explore.html',{})