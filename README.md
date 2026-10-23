# Flask Weather App

A single-page weather app using Python, Flask, Requests, and python-dotenv. Enter a city, state/province, and country to display current weather in Celsius.

## Features
- Form submits location details with POST.
- OpenWeather Geocoding API converts the location to coordinates.
- OpenWeather Current Weather API retrieves current conditions.
- Displays condition, description, icon, temperature, feels-like temperature, and humidity.
- API key is loaded from `.env`; `.env` is excluded from Git.

## Requirements
- Python 3.10+
- An OpenWeather API key (new keys may take time to activate).

## Setup (Windows PowerShell)
1. Open this folder in VS Code.
2. Create and activate a virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Create your local environment file:
   ```powershell
   Copy-Item .env.example .env
   ```
5. Open `.env` and replace the placeholder with your real key:
   ```text
   OPENWEATHER_API_KEY=your_actual_api_key
   ```
   Never commit or share `.env`; upload only `.env.example`.
6. Run:
   ```powershell
   python app.py
   ```
7. Visit http://127.0.0.1:5000

Try `Kalaburagi`, `Karnataka`, `India`.

## Project structure
```text
weather-app-flask/
├── app.py
├── weather.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## Notes
The app needs an internet connection and a valid OpenWeather API key. This is a learning project, not a production weather service. Debug mode is for local development only. If a real key is accidentally committed publicly, revoke it and create a new one.
