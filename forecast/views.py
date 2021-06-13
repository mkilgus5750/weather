from django.shortcuts import render
from django.http import HttpResponse
import requests
from utils import API_KEY 
# Create your views here.

def index(request, city):
    # make request
    url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&aqi=no&alerts=no'

    headers = {
        'cache-control': "no-cache",
        }

    response = requests.request("GET", url, headers=headers)
    res_data = response.json()
    city_name = res_data['location']['name']
    region = res_data['location']['region']
    country = res_data['location']['country']
    localtime = res_data['location']['localtime']
    current_condition_string = res_data['current']['condition']['text']
    current_condition_image = res_data['current']['condition']['icon']
    current_temp_f = res_data['current']['temp_f']
    feelslike_f = res_data['current']['feelslike_f']
    three_day_forecast = res_data['forecast']['forecastday']

    return render(request, 'forecast/index.html', {
        'city_name': city_name,
        'region': region,
        'country': country,
        'localtime': localtime,
        'current_condition_string': current_condition_string,
        'current_condition_image': current_condition_image,
        'current_temp_f': current_temp_f,
        'feelslike_f': feelslike_f,
        'three_day_forecast' : three_day_forecast
    })