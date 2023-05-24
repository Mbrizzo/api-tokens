from web3 import Web3
import requests
import sys

from dotenv import load_dotenv
import os

load_dotenv()
bsc_api_key = os.getenv('api_key')

web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

contract_address = ''

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

if contract_abi is None:
    print('Não foi possível obter a ABI do contrato')
    sys.exit()

bytecode = web3.eth.getCode(contract_address).hex()
if bytecode == '0x':
    print('Iniciando outros testes de segurança')
else:
    print('O contrato não é seguro! ')

def is_contract_renounced(contract_address, contract_abi):
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    renounced = contract.functions.owner().call() == '0x0000000000000000000000000000000000000000'
    return renounced

contract_renounced = is_contract_renounced(contract_address, contract_abi)

if contract_renounced:
    print('O contrato está renunciado')
else:
    print('O contrato não está renunciado')

def check_gas(contract):
    low_gas_limit = 10000
    for function in contract.abi:
        if function['type'] == 'function':
            gas_limit = function['gas']
            if gas_limit < low_gas_limit:
                return True
    return False