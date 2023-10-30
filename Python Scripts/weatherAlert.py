# program to send an alert

import requests

# Constants
API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
CITY = 'YOUR_CITY'
COUNTRY_CODE = 'YOUR_COUNTRY_CODE'
THRESHOLD_TEMPERATURE = 273.15 + 30  # 30°C in Kelvin. Adjust accordingly.


def get_weather_data(city, country_code, api_key):
    """Fetch weather data for a given city using OpenWeatherMap."""
    url = f"{BASE_URL}?q={city},{country_code}&appid={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        print(
            f"Failed to retrieve weather data. Status code: {response.status_code}")
        return None

    return response.json()


def send_alert(message):
    """Send alert message. For simplicity, we're just printing the message. This can be enhanced to send emails or notifications."""
    print(message)


if __name__ == "__main__":
    weather_data = get_weather_data(CITY, COUNTRY_CODE, API_KEY)

    if not weather_data:
        print("No weather data available.")
    else:
        main_temp = weather_data['main']['temp']

        if main_temp > THRESHOLD_TEMPERATURE:
            send_alert(
                f"Temperature Alert in {CITY}: {main_temp - 273.15}°C. Stay hydrated and avoid direct sunlight!")
        else:
            print(
                f"Weather is normal in {CITY}. Temperature: {main_temp - 273.15}°C")
