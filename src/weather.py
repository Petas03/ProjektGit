import requests
import json

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city):
        try:
            url = f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            data = response.json()
            return self.parse_weather_data(data)
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def get_weather_by_ip(self, ip_address):
        try:
            # Get location info
            location_url = f"https://ipapi.co/{ip_address}/json/"
            location_response = requests.get(location_url)
            location_response.raise_for_status()
            location_data = location_response.json()
            city = location_data.get('city')
            if city:
                return self.get_weather_by_city(city)
            else:
                return {"error": "City not found in location data."}
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def parse_weather_data(self, data):
        if "main" in data:
            weather_info = {
                "temperature": data["main"]["temp"],
                "pressure": data["main"]["pressure"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"]
            }
            return weather_info
        return {"error": "Weather data not found."}

# Example Usage:
if __name__ == '__main__':
    api_key = 'YOUR_API_KEY'  # Replace with your actual OpenWeatherMap API key
    weather_api = WeatherAPI(api_key)
    ip_address = 'YOUR_IP_ADDRESS'  # Replace with the actual IP address you want to check
    print(weather_api.get_weather_by_ip(ip_address))
