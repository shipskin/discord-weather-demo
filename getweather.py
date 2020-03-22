# OpenWeather API KEY: e2ce1e4408734e2c1500876cd106a8f0
import requests

#request to openweather
def get_weather(cityname,state):
    openweather_apikey = 'e2ce1e4408734e2c1500876cd106a8f0'
    while True:
        try:
            if state:
                r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid={}'.format(cityname,state,openweather_apikey))
            else:
                r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'.format(cityname,openweather_apikey))
            return(r.json())
        except:
            print('Invalid request, check the city name')

# get input
cityname = input('city - ')
state = input('state(country) - ')

#JSON returned from OpenWeather
json_weather = get_weather(cityname, state)

#print a nice little ditty
print('Feels like {}F with {} in {}.'.format(json_weather['main']['feels_like'],json_weather['weather'][0]['description'],json_weather['name']))
