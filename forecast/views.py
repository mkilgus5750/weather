from django.shortcuts import render
from django.http import HttpResponse
import requests
from utils import API_KEY 
import datetime

# Create your views here.
def icon(condition):
    if condition == 'Sunny':
        return 'Sunny'
    elif 'cloudy' in condition.lower() or 'overcast' in condition.lower():
        return 'cloudy'
    elif 'rain' in condition.lower() or 'drizzle' in condition.lower():
        return 'rain'
    elif 'snow' in condition.lower():
        return 'flurries'
    elif 'thunder' in condition.lower():
        return 'thunder_storm'
    else:
        return 'sunny'

def index(request, city):
    # make request
    url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=5&aqi=no&alerts=no'

    headers = {
        'cache-control': "no-cache",
        }

    response = requests.request("GET", url, headers=headers)
    res_data = response.json()
    location = res_data['location']
    current = res_data['current']
    three_day_forecast = res_data['forecast']['forecastday']
    string_days_of_week = [datetime.datetime.strptime(day['date'], '%Y-%m-%d').strftime('%a') for day in three_day_forecast]
    condition = icon(current['condition']['text'])

    return render(request, 'forecast/index.html', {
        'location': location,
        'current': current,
        'three_day_forecast': three_day_forecast,
        'string_days_of_week': string_days_of_week,
        'condition': condition
    })