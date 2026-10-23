import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from weather import get_weather_for_location

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    data, error = None, None
    city, state, country = "", "Karnataka", "India"
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        country = request.form.get("country", "").strip()
        if not city or not country:
            error = "Please enter at least a city and country."
        elif not os.getenv("OPENWEATHER_API_KEY"):
            error = "API key missing. Add OPENWEATHER_API_KEY to your local .env file."
        else:
            try:
                data = get_weather_for_location(city, state, country)
                if data is None:
                    error = "Location not found. Check the city, state, and country."
            except Exception as exc:
                error = str(exc)
    return render_template("index.html", data=data, error=error, city=city, state=state, country=country)

if __name__ == "__main__":
    # Debug mode is intended for local development only.
    app.run(debug=True)
