from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests, json, datetime
from .models import Culeba

def ajax(request):
    if request.method == "POST":
        
        objs = json.loads(request.body.decode("utf-8"))
        date_id = objs.get('text')
        y = Culeba.objects.filter(date__gte = date_id)[:9]
        
        d = datetime.date.today()
        x = Culeba.objects.filter(date__gte = d)
        print(len(x))

        dt_t = [i.time[:5] for i in y]
        temp = [(float(i.temp_max) + float(i.temp_min))/2.0 for i in y]
        dt_p = [i.date[-2:] + "-го " + i.time[:5] for i in x]
        pres = [i.pressure for i in x]
        
        return JsonResponse({'dt_t' : dt_t, 'temp': temp, 'dt_p' : dt_p, 'pres': pres})

def owmo(request):
    
    d = datetime.date.today()
    x = Culeba.objects.filter(date__gte = d)
    
    try:
        city_name = [x[0].name, x[0].lon, x[0].lat]
        step = sorted(set([i.date for i in x]))
        for_table = [[i.date, i.time[:-3], i.temp_max, i.temp_min, i.wind, i.cloud, i.pressure, i.description] for i in x]

    except:
        return HttpResponse('Try later')

    return render(request, 'nodeads/city.html', {'city_name': city_name, 'step': step, 'for_table': for_table})


def owm(request):
    
    forecast = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=703448&APPID=7fa1442d92205c9553fd4a96f58d42e3&units=metric&lang=uk")
    
    try:
        if forecast['city']['name'] == "Kiev":
            for i in forecast['list']:
                c = Culeba()
                c.name = forecast['city']['name']
                c.lon = forecast['city']['coord']['lon']
                c.lat = forecast['city']['coord']['lat'] 
                c.date = i['dt_txt'].split()[0]
                c.time = i['dt_txt'].split()[1]
                c.temp_max = i['main']['temp_max']
                c.temp_min = i['main']['temp_min']
                c.wind = i['wind']['speed']
                c.cloud = i['clouds']['all']
                c.pressure = i['main']['pressure']
                c.description = i['weather'][0]['description']
                try:
                    x = Culeba.objects.get(date = c.date, time = c.time)
                    if x.time != c.time:
                        c.save()
                except:
                    pass
    except:
        pass
    
    return redirect('owmo/')
