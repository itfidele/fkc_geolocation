from django.shortcuts import render
import requests
import json
# Create your views here.

def get_client_ip(request):
    x_forward_for = request.META.get("HTTP_X_FORWARDED_FOR")
    
    if x_forward_for:
        ip = x_forward_for.split(',')[-1]
        print(ip)
    else:
        ip = request.META.get("REMOTE_ADDR")
    
    return ip


def index(request):
    ip = get_client_ip(request)
    res = requests.get(f'http://ip-api.com/json/41.75.188.86')
    # res = requests.get(f'https://api.iplocation.net/?cmd=ip-country&ip={ip}')
    location_data_one = res.text
    print(location_data_one)
    location_data = json.loads(location_data_one)
    # weather_info = request.get(f"http://api.openweathermap.org/data/2.5/weather?lat={location_data['lat']}&lon={location_data['lon']}&appid=API_KEY")
    return render(request, 'index.html', {'data': location_data,'flag':f"http://countryflagsapi.com/png/{location_data['countryCode']}"})
