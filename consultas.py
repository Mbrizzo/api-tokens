import requests
import json

from dotenv import load_dotenv
import os

load_dotenv()
bscscan_api_key = os.getenv('api_key')

url_base = 'https://api.bscscan.com/api'

def contract_internal():
    url = f'{url_base}=txlistinternal&address=0x0000000000000000000000000000000000001004&startblock=0&endblock=999999999&sort=desc&apikey={bscscan_api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def get_last_block():
    url = f'{url_base}?module=proxy&action=eth_blockNumber&apikey={bscscan_api_key}'
    response = requests.get(url)
    data = response.json()
    block_number = int(data['result'], 16)  # Converter o número do bloco hexadecimal para inteiro
    return block_number

def get_block_details(block_number):
    url = f'{url_base}?module=proxy&action=eth_getBlockByNumber&tag={block_number}&boolean=true'
    response = requests.get(url)
    data = response.json()
    return data

block_number = get_last_block()
block_details = get_block_details(block_number)
print(block_details)


