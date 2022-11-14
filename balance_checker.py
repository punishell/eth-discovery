import sys
import os
import requests
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware
from web3 import Web3

ethplorer_token = os.getenv('ETHP_TOKEN', None)

for line in sys.stdin:

    private_key = line.strip()
    try:
        account: LocalAccount = Account.from_key(private_key)
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
        print(f"Your PRIVATE_KEY is {private_key}")
        print(f"Your hot wallet address is {account.address}")

        rpc_url = "https://eth-mainnet.nodereal.io/v1/1659dfb40aa24bbb8153a677b98064d7"
        r = requests.get(url='https://api.ethplorer.io/getAddressInfo/' + account.address + '?apiKey=' + ethplorer_token +"&showETHTotals=true")
        web3 = Web3(Web3.HTTPProvider(rpc_url))
        print(f"Your ETH Balance is:{web3.eth.getBalance(account.address)}")
        #print(r.json())
        for token in r.json()['tokens']:
            print(f"Token Name: {token['tokenInfo']['name']}")
            print(f"Token address: {token['tokenInfo']['address']}")            
            print(f"Token balance: {token['balance']}")
            print(f"\n")
        # print(f"Your ETH IN/OUT BALANCE wiht tokens: {r.json()['totalIn']}")
        print("-------------------------------------------------------------\n")
    except:
        print("An exception occurred")
