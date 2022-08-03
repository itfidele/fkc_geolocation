from django.shortcuts import render
import requests
import json
# Create your views here.

def index(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    ip = ip_data['ip']
    res = requests.get(f'http://ip-api.com/json/{ip}')
    # res = requests.get(f'https://api.iplocation.net/?cmd=ip-country&ip={ip}')
    location_data_one = res.text
   
    location_data = json.loads(location_data_one)
    # weather_info = request.get(f"http://api.openweathermap.org/data/2.5/weather?lat={location_data['lat']}&lon={location_data['lon']}&appid=API_KEY")
    return render(request, 'index.html', {'data': location_data})
