# Weather AI Agent 

A Python app that fetches live weather for any city in the world 
and uses AI to give a friendly summary and outfit recommendation.

## What it does
- Takes a city name from the user
- Fetches live coordinates using a geocoding API
- Gets real time weather data from Open-Meteo
- Passes the data to OpenAI GPT for a natural language summary

## Built with
- Python
- Open-Meteo API (weather + geocoding)
- OpenAI GPT-3.5
- requests, python-dotenv

## How to run
1. Clone the repo
2. Create a virtual environment and activate it
3. Run `pip install -r requirements.txt`
4. Add your OpenAI API key to a `.env` file
5. Run `python main.py`