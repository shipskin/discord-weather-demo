import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
DISCORD_CLIENT = os.getenv('DISCORD_CLIENT')