import network
import socket
import time
import machine
import urequests
import lcd

# WiFi Connection Information
SSID = 'your_ssid'
PASSWORD = 'your_password'

# LCD Pin Configuration
lcd_init = lcd.LCD(pins={'rs': 21, 'e': 22, 'd4': 23, 'd5': 24, 'd6': 25, 'd7': 26})

# Function to connect to WiFi
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    return wlan.ifconfig()

# Function to get location from IP API
def get_location():
    response = urequests.get('https://ipapi.co/json/')
    return response.json()

# Function to fetch weather data from API
def fetch_weather(location):
    endpoint = f'http://api.weatherapi.com/v1/current.json?key=your_api_key&q={location}'
    response = urequests.get(endpoint)
    return response.json()

# Function to display weather on LCD
def display_weather(data):
    lcd_init.clear()
    weather = f"{data['current']['temp_c']}°C\n{data['current']['condition']['text']}"
    lcd_init.write(weather)

# Main program entry point
if __name__ == '__main__':
    connect_wifi(SSID, PASSWORD)
    location_data = get_location()
    while True:
        weather_data = fetch_weather(location_data['city'])
        display_weather(weather_data)
        time.sleep(600)  # Fetch weather data every 10 minutes
