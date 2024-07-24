import requests
import os
def clear():
  if os.name=='nt':
    os.system('cls')
  else:
    os.system('clear')
clear()
def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        
        weather_report = (f"City: {city}\n"
                          f"Temperature: {temperature}°C\n"
                          f"Humidity: {humidity}%\n"
                          f"Description: {description}")
        
        return weather_report
    else:
        return "City not found. Please enter a valid city name."

if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))
