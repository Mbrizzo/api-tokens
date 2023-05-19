import requests

from dotenv import load_dotenv
import os

load_dotenv()
bscscan_api_key = os.getenv('api_key')

url_base = 'https://api.bscscan.com/api?module'

def contract_internal():
    url = f'{url_base}=txlistinternal&address=0x0000000000000000000000000000000000001004&startblock=0&endblock=999999999&sort=desc&apikey={bscscan_api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def get_last_block():
    url = f'{url_base}=proxy&action=eth_blockNumber&apikey={bscscan_api_key}'
    response = requests.get(url)
    data = response.json()
    return data

block = get_last_block()
print(block)




