import requests
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("API_KEY")
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"


# def fetch_data():
#     print("Fetching weather data from Weatherstack API ....  ")
#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()
#         print("API response recieved successfully")
#         return response.json()
#         #print(response.json())
#     except requests.exceptions.RequestException as e:
#         print(f"An error occured: {e}")
#         raise
    

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-11-22 08:43', 'localtime_epoch': 1763800980, 'utc_offset': '-5.0'}, 'current': {'observation_time': '01:43 PM', 'temperature': 8, 'weather_code': 296, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0017_cloudy_with_light_rain.png'], 'weather_descriptions': ['Light Rain, Mist'], 'astro': {'sunrise': '06:51 AM', 'sunset': '04:33 PM', 'moonrise': '09:21 AM', 'moonset': '05:56 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 3}, 'air_quality': {'co': '491.85', 'no2': '29.35', 'o3': '23', 'so2': '10.85', 'pm2_5': '22.65', 'pm10': '22.75', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 9, 'wind_degree': 3, 'wind_dir': 'N', 'pressure': 1012, 'precip': 0.7, 'humidity': 90, 'cloudcover': 100, 'feelslike': 7, 'uv_index': 0, 'visibility': 6, 'is_day': 'yes'}}