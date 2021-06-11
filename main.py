import requests
from datetime import datetime

user_api = "4c4c334f055a2b046735e186fe6fbe2a"
location = input("Enter the city name ")
complet_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complet_api_link)
api_data = api_link.json()

if api_data["cod"] == "404":
    print("Invalid City: {}, Please check your City name".format(location))
else:
    temp_city = ((api_data["main"]["temp"]) - 273.15)
    weather_desc = api_data["weather"][0]["description"]
    hmdt = api_data["main"]["humidity"]
    wind_spd = api_data["wind"]["speed"]
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-----------------------------------------------------------------")
    print("Weather stats for - {} || {}".format(location.upper(), date_time))
    print("-----------------------------------------------------------------")

    print("Current temperature is : {:.2f} deg C".format(temp_city))
    print("Current weather desc   :", weather_desc)
    print("Current Humidity       :", hmdt,"%")
    print("Current wind speed     :",wind_spd, "kmph")