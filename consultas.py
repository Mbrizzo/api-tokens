import requests

from dotenv import load_dotenv
import os

load_dotenv()

bscscan_api_key = os.getenv('api_key')

url = f'https://api.bscscan.com/api?module=account&action=txlistinternal&address=0x0000000000000000000000000000000000001004&startblock=0&endblock=999999999&sort=desc&apikey={bscscan_api_key}'
response = requests.get(url)
data = response.json()

print(data)