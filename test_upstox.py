import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("INDIAN_API_KEY")

headers = {
    "x-api-key": API_KEY,
    "accept": "application/json"
}

url = "https://stock.indianapi.in/stock"

params = {
    "name": "Infosys"
}

response = requests.get(
    url,
    headers=headers,
    params=params
)

print("Status:", response.status_code)
print(response.text)