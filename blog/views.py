from django.shortcuts import render
from blog.models import Location
from blog.models import Food
from blog.models import Transport
import requests
import json


# Create your views here.


def show(request):
  
    
    headers = {'X-API-KEY':'PATRICKONEILL04032020','Content-Type':'application/json'}
    response = requests.get('https://www.budgetyourtrip.com/api/v3/countries', headers=headers)
    geodata = response.json()
    geodata = geodata['data']
    #geodata = geodata[0]['name']

        
    content = []
    
    for x in geodata:
        content.append(x['name'])

    return render(request, 'blog/post_list.html', {'name':content})




def results(request):
    loc= Location.objects.values('location')
    foo= Food.objects.all()
    trans= Transport.objects.values('transport')
    
    content = {
    'location':loc,
    'food':foo,
    'transport':trans,
    }
    return render(request, 'blog/results.html', content)





