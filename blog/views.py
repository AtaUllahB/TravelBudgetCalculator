from django.shortcuts import render
from blog.models import Location
from blog.models import Food
from blog.models import Transport
import requests
import json


# Create your views here.


def show(request):
  
    user1 = []
    response2 = {}
    response3={}
    response4={}
    test2 =[]
    cit = []
    cit1 = []
    cit2 = []
    cit3 = []
    cit4 = []
    cit5 = []
    if 'query' in request.GET:
        username = request.GET['query']
        username = (username[-2]+username[-1])
        headers = {'X-API-KEY':'PATRICKONEILL04032020','Content-Type':'application/json'}
        url = 'https://www.budgetyourtrip.com/api/v3/costs/countryinfo/%s' % username
        response = requests.get(url, headers=headers)
        response1 = ((((response.json())['data']["costs"])))
        response2 = ((response.json())['data']["info"]["currency_code"])
        response3 = ((response.json())['data']["info"]["name"])
        for x in response1:
            user1.append(x)
        
        headers = {'X-API-KEY':'PATRICKONEILL04032020','Content-Type':'application/json'}
        url = 'https://www.budgetyourtrip.com/api/v3/costs/countryhighlights/%s' % username
        response = requests.get(url, headers=headers)
        response4 = ((response.json())['data'])
        
       
       
  
    if 'sel1' in request.GET: 
        cit = request.GET['sel1']
        headers = {'X-API-KEY':'PATRICKONEILL04032020','Content-Type':'application/json'}
        url = 'https://www.budgetyourtrip.com/api/v3/costs/locationinfo/%s' %cit
        response = requests.get(url, headers=headers)
        cit1 = ((((response.json())['data']["costs"])))
        cit2 = ((response.json())['data']["info"]["asciiname"])
        cit3 = ((response.json())['data']["info"]["currency_code"])
        
        
        headers = {'X-API-KEY':'PATRICKONEILL04032020','Content-Type':'application/json'}
        url = 'https://www.budgetyourtrip.com/api/v3/activities/citysearch/%s' %cit2
        response = requests.get(url, headers=headers)
        cit4 = ((response.json())['data'])
        
        headers = {'X-API-KEY':'PATRICKONEILL04032020','Content-Type':'application/json'}
        url = 'https://www.budgetyourtrip.com/api/v3/costs/highlights/%s' %cit
        response = requests.get(url, headers=headers)
        cit5 = ((response.json())['data'])
        
        
            
        
    headers = {'X-API-KEY':'PATRICKONEILL04032020','Content-Type':'application/json'}
    response = requests.get('https://www.budgetyourtrip.com/api/v3/currencies', headers=headers)
    test1 = response
    test1 = ((response.json())['data'])
    #test1 = test1['currency_code']
    #test1 == ((((response.json())['data']["currency_code"])))
    for x in test1:
        test2.append((x["currency_code"]))
    
    headers = {'X-API-KEY':'PATRICKONEILL04032020','Content-Type':'application/json'}
    response = requests.get('https://www.budgetyourtrip.com/api/v3/countries', headers=headers)
    geodata = response.json()
    geodata = geodata['data']
    #geodata = geodata[0]['name']
    content = []
    for x in geodata:
        content.append((x["name"]+" "+x["country_code"]))
        
    return render(request, 'blog/blog.html', {'name':content, 
                                                   'username':user1,
                                                   'username2':response2,
                                                   'username3':response3,
                                                   'response4':response4,
                                                   'test1':test2,
                                                   'cit1':cit1,
                                                   'cit2':cit2,
                                                   'cit3':cit3,
                                                   'cit4':cit4,
                                                   'cit5':cit5})




#def results(request):
 #   loc= Location.objects.values('location')
  #  foo= Food.objects.all()
   # trans= Transport.objects.values('transport')
    
    #content = {
    #'location':loc,
    #'food':foo,
    #'transport':trans,
    #}
    #return render(request, 'blog/results.html', content)

