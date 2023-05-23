from web3 import Web3
import sys

web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

contract_address = ''

def get_contract_abi(contract_address):
    bytecode = web3.eth.getCode(contract_address)
    if bytecode == '0x':
        return None
    transaction = {'to': contract_address, 'data': '0x'}
    try:
        call = web3.eth.call(transaction)
        abi = web3.eth.contract(abi=call).abi
        return abi
    except:
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