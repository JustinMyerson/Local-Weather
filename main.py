# This is a Python script to provide the local weather information
# Requests will be made to the Open Weather Map API and the data will be returned in JSON format
import requests
import json


def convertKelvinToCelsius(temperature):
    """
    convertKelvinToCelsius takes a float temperature measurement in Kelvin and returns an int with the temperature in Celsius

    :temperature The temperature provided in Kelvin
    :return Returns the temperature in Celsius
    """
    return int(temperature - 273.15)


# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
CITY = "Cape Town"

# Your API key
API_KEY = "7e136c59e5679b57826401187b55d851"

# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)

# Indicating the data was successfully fetched
if response.status_code == 200:
    data = response.json()
    main = data['main']

    weather = data['weather']

    # API returns weather as Kelvin, so need to convert to Celsius
    temperature = convertKelvinToCelsius(main['temp'])
    real_feel = convertKelvinToCelsius(main['feels_like'])

    print(f"Today's weather: {weather[0]['description'].capitalize()}")
    print(f"Temperature: {temperature}")
    print(f"Real Feel: {real_feel}")
else:
    print("Error fetching data from API")
