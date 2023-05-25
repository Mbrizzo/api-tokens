import requests
from web3 import Web3

from dotenv import load_dotenv
import os

load_dotenv()
infura_id = os.getenv('infura_id')
bsc_api_key = os.getenv('bsc_api_key')

infura_url = f"https://bsc.infura.io/v3/{infura_id}"
web3 = Web3(Web3.HTTPProvider(infura_url))

contract_address = "0x990ca0162b66e187ABd87E816A33589E2dCcCeDa"

def get_contract_abi(contract_address):
    url = f'https://api.bscscan.com/api?module=contract&action=getabi&address={contract_address}&apikey={bsc_api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if result['status'] == '1':
            abi = result['result']
            return abi
    return None

contract_abi = get_contract_abi(contract_address)

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

functions = contract.all_functions()

for function in functions:
    print(function.fn_name)
