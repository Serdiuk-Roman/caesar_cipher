from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests, json, datetime, collections
from .models import Culeba
from urllib.request import urlopen

def ajax(request):
    if request.method == "POST":
        
        objs = json.loads(request.body.decode("utf-8"))
        date_id = objs.get('text')
        full_temp = Culeba.objects.filter(date__gte = date_id)[:9]
        
        d = datetime.date.today()
        full_pres = Culeba.objects.filter(date__gte = d)

        dt_t = [i.time[:5] for i in full_temp]
        temp = [(float(i.temp_max) + float(i.temp_min))/2.0 for i in full_temp]
        dt_p = [i.date[-2:] + "-го " + i.time[:5] for i in full_pres]
        pres = [i.pressure for i in full_pres]
        
        return JsonResponse({'dt_t' : dt_t, 'temp': temp, 'dt_p' : dt_p, 'pres': pres})

def owmo(request):
    
    d = datetime.date.today()
    x = Culeba.objects.filter(date__gte = d)
    
    #little table
    
    date_lt = sorted(set([i.date for i in x]))

    #time_lt = sorted(set([j.time for j in x]))
    
    little_table = [[x] for x in date_lt]
    counter = 0
    for j in date_lt:
        
        db_lt = Culeba.objects.filter(date = j)
        little_table[counter].append(max([float(k.temp_max) for k in db_lt]))
        little_table[counter].append(min([float(k.temp_min) for k in db_lt]))
        y = [float(k.wind) for k in db_lt]
        little_table[counter].append(round(sum(y)/len(y), 2))
        z = [float(k.cloud) for k in db_lt]
        little_table[counter].append(round(sum(z)/len(z), 2))
        m = [float(k.pressure) for k in db_lt]
        little_table[counter].append(round(sum(m)/len(m), 2))
        n = [k.description for k in db_lt]
        n2 = [i[0] for i in collections.Counter(n).most_common(1)]
        little_table[counter].append(n2[0])
        counter += 1
    
    #big table
    
    city_name = [x[0].name, x[0].lon, x[0].lat]
    step = sorted(set([i.date for i in x]))
    for_table = [[i.date, i.time[:-3], i.temp_max, i.temp_min, i.wind, i.cloud, i.pressure, i.description] for i in x]

    return render(request, 'nodeads/city.html', {'city_name': city_name, 'step': step, 'for_table': for_table, 'little_table': little_table})


def owm(request):
    
    request_api = urlopen("http://api.openweathermap.org/data/2.5/forecast?id=703448&APPID=7fa1442d92205c9553fd4a96f58d42e3&units=metric&lang=uk")
    request_api2 = request_api.read().decode('utf-8')
    forecast = json.loads(request_api2)
    
    for i in forecast['list']:
        c = Culeba()
        c.date = i['dt_txt'].split()[0]
        c.time = i['dt_txt'].split()[1]
        x = Culeba.objects.filter(date = c.date).filter(time = c.time)
        if not x:
            c.name = forecast['city']['name']
            c.lon = forecast['city']['coord']['lon']
            c.lat = forecast['city']['coord']['lat']
            c.temp_max = i['main']['temp_max']
            c.temp_min = i['main']['temp_min']
            c.wind = i['wind']['speed']
            c.cloud = i['clouds']['all']
            c.pressure = i['main']['pressure']
            c.description = i['weather'][0]['description']
            c.save()                
        x = None
        c = None

    return redirect('owmo/')
