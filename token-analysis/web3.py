from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

contract_address = ''

def is_honeypot(address):
    bytecode = web3.eth.getCode(address).hex()
    if bytecode == '0x':
        return False
    else:
        return True

result = is_honeypot(contract_address)

def check_gas(contract):
    low_gas_limit = 10000
    for function in contract.abi:
        if function['type'] == 'function':
            gas_limit = function['gas']
            if gas_limit < low_gas_limit:
                return True
    return False

result = is_honeypot(contract_address)