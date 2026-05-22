import requests
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#collecting user input
city = input("Enter the city name: ").strip()
try:
    headers = {"User-Agent": "weather-agent/1.0"}
    geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"

    response = requests.get(geo_url, headers=headers)
    data = response.json()
    if  len(data) == 0:
        print("city not found.Try again!")

    else:
        latitude = data[0]['lat']
        longitude = data[0]['lon']

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    weather_response = requests.get(weather_url)
    weather_data = weather_response.json()

    weather = weather_data['current_weather']

    temperature = weather['temperature'] 
    wind_speed = weather['windspeed']

    print(f"\nCurrent weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Wind Speed: {wind_speed} km/h")

        # Ask OpenAI to summarise the weather
    ai_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"The weather in {city} is {temperature}°C with a windspeed of {wind_speed} km/h. Give a short friendly summary and what I should wear today."
            }
        ]
    )

    print("\nAI Summary:")
    print(ai_response.choices[0].message.content)

except requests.exceptions.ConnectionError:
    print("Network error. Please check your internet connection and try again.")

except Exception as e:
    print(f"An error occurred: {e}")    


        