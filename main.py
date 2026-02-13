import network
import time
import urequests
import machine
from machine import Pin, I2C
import ssd1306

# Constants
SSID = 'your_wifi_ssid'
PASSWORD = 'your_wifi_password'
API_KEY = 'your_openweathermap_api_key'
LOCATION_API_URL = 'http://ip-api.com/json/'
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

# LCD setup
I2C_SCL = 22
I2C_SDA = 21
WIDTH = 128
HEIGHT = 64

# Connect to WiFi
wifi = network.WLAN(network.STA_IF)

# Function to connect to WiFi
def connect_to_wifi():
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)
    print('Connecting to WiFi...')
    while not wifi.isconnected():
        time.sleep(1)
    print('Connected to WiFi:', wifi.ifconfig())

# Function to get location
def get_location():
    response = urequests.get(LOCATION_API_URL)
    return response.json()['city'] if response.status_code == 200 else 'Unknown'

# Function to fetch weather
def fetch_weather(city):
    url = f'{WEATHER_API_URL}?q={city}&appid={API_KEY}&units=metric'
    response = urequests.get(url)
    return response.json() if response.status_code == 200 else None

# Function to display on LCD
def display_lcd(text):
    i2c = I2C(-1, Pins=(I2C_SDA, I2C_SCL))
    oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
    oled.fill(0)
    oled.text(text, 0, 0)
    oled.show()

# Main function
def main():
    connect_to_wifi()
    city = get_location()
    while True:
        weather_data = fetch_weather(city)
        if weather_data:
            weather_desc = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            display_lcd(f'Temp: {temp}°C\nWeather: {weather_desc}')
        else:
            print('Failed to fetch weather data. Retrying...')
        time.sleep(600)  # 10 minutes delay

if __name__ == '__main__':
    main()