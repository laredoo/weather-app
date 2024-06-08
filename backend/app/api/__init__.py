from dotenv import load_dotenv
import os

load_dotenv("/Users/lucas/sandbox/weather-app/backend/app")

api_key = os.getenv('API_KEY')

print(f"A sua API key é: {api_key}")
