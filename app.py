import discord
import requests
import urllib.parse
from settings import WEATHER_API_KEY, DISCORD_CLIENT

client = discord.Client()

def get_weather_icon(id):
    if id <= 300:
        return ":cloud_lightning:"
    elif id <= 600:
        return ":cloud_rain:"
    elif id <= 700:
        return ":cloud_snow:"
    elif id < 800:
        return ":cloud:"
    elif id == 800:
        return ":sunny:"
    else:
        return ":cloud:"

#request to openweather
def get_weather(cityname=None, state=None):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    std_query = f'&units=imperial&appid={WEATHER_API_KEY}'
    try:
        cityname = urllib.parse.quote(cityname)
        if state:
            state = urllib.parse.quote(state)
            query = f'q={cityname},{state}'
        else:
            query = f'q={cityname}'
        r = requests.get(f'{base_url}{query}{std_query}')
        print(r.text)
        print(r.status_code)
        if r.status_code == 200:
            return(r.json())
        else:
            return False
    except:
        print('Invalid request, check the city name')
        return False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        print('client user: ', client.user)
        return

    bot_word = '$weather'
    if message.content.startswith(bot_word):
        content = message.content.replace(bot_word, '').strip()
        if ',' in content:
            city, state = content.split(',')
            city = city.strip()
            state = state.strip()
        else:
            city = content.strip() if content else 'san francisco'
            state = 'us'
        response = get_weather(cityname=city, state=state)
        print(response)
        if response:
            weather_id = response['weather'][0]['id']
            weather_icon = get_weather_icon(weather_id)
            feels_like = response['main']['feels_like']
            description = response['weather'][0]['description']
            city_name = response['name']
            text = f'{weather_icon} It feels like {feels_like}°F with {description} in {city_name}'
        else:
            text = "woops can't find that city"
        
        await message.channel.send(text)



client.run(DISCORD_CLIENT)

