import os
from dataclasses import dataclass
import requests
from dotenv import load_dotenv

load_dotenv()
GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct"
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: float
    feels_like: float
    humidity: int
    city_name: str

def get_lat_long(city: str, state: str, country: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY is not set in .env.")
    location = ",".join(part for part in (city, state, country) if part)
    response = requests.get(GEOCODING_URL, params={"q": location, "limit": 1, "appid": api_key}, timeout=15)
    response.raise_for_status()
    results = response.json()
    if not results:
        return None
    return results[0]["lat"], results[0]["lon"]

def get_current_weather(latitude: float, longitude: float) -> dict:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENWEATHER_API_KEY is not set in .env.")
    response = requests.get(
        CURRENT_WEATHER_URL,
        params={"lat": latitude, "lon": longitude, "appid": api_key, "units": "metric"},
        timeout=15,
    )
    response.raise_for_status()
    return response.json()

def get_weather_for_location(city: str, state: str, country: str):
    coordinates = get_lat_long(city, state, country)
    if coordinates is None:
        return None
    raw = get_current_weather(*coordinates)
    weather = (raw.get("weather") or [{}])[0]
    main = raw.get("main") or {}
    return WeatherData(
        main=weather.get("main", "Unknown"),
        description=weather.get("description", "No description available").title(),
        icon=weather.get("icon", "01d"),
        temperature=round(float(main.get("temp", 0))),
        feels_like=round(float(main.get("feels_like", 0))),
        humidity=int(main.get("humidity", 0)),
        city_name=raw.get("name", city),
    )
