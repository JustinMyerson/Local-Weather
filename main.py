# Requests will be made to the Open Weather Map API and the data will be returned in JSON format
import requests
import json

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
CITY = "New Delhi"

# Your API key
API_KEY = "7e136c59e5679b57826401187b55d851"

# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

response = requests.get(URL)
data = response.json()

print(data)
