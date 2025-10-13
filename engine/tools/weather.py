from langchain.tools import tool
import requests

@tool("weather", return_direct=True)
def get_weather(location: str) -> str:
    """Get current weather data using Open-Meteo (no API key required)."""
    try:
        # Geocoding (to get latitude/longitude)
        geo = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={location}"
        ).json()
        if "results" not in geo or not geo["results"]:
            return f"Could not find location: {location}"

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]
        city = geo["results"][0]["name"]

        # Fetch weather data
        weather = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weathercode,wind_speed_10m"
        ).json()
        current = weather["current"]
        temp = current["temperature_2m"]
        wind = current["wind_speed_10m"]

        return f"🌤️ Weather in {city}: {temp}°C, wind speed {wind} km/h."

    except Exception as e:
        return f"Error fetching weather: {e}"
