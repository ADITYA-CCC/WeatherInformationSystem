from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather():
    city = request.args.get('city', '').strip()

    if not city:
        return render_template(
            'index.html',
            error="Please enter a city name."
        )

    try:
        # Step 1: Get city coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        geo_response.raise_for_status()
        geo_data = geo_response.json()

        print("Geocoding API Response:", geo_data)

        if not geo_data.get("results"):
            return render_template(
                'index.html',
                error="City not found. Please try again."
            )

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Step 2: Get weather information
        weather_url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
            "timezone": "auto"
        }

        response = requests.get(
            weather_url,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        print("Weather API Response:", data)

        current = data["current"]

        weather_info = {
            "city": location["name"],
            "country": location.get("country", ""),
            "temperature": current["temperature_2m"],
            "feels_like": current["apparent_temperature"],
            "humidity": current["relative_humidity_2m"],
            "wind": current["wind_speed_10m"],
            "precipitation": current["precipitation"]
        }

        return render_template(
            'index.html',
            weather=weather_info
        )

    except Exception as e:
        print("ERROR:", str(e))

        return render_template(
            'index.html',
            error=f"Unable to fetch weather information: {str(e)}"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
