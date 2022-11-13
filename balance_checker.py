import sys
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3.auto import w3
from web3.middleware import construct_sign_and_send_raw_middleware
from web3 import Web3

for line in sys.stdin:

    private_key = line.strip()

    account: LocalAccount = Account.from_key(private_key)
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
    print(f"Your PRIVATE_KEY is {private_key}")
    print(f"Your hot wallet address is {account.address}")

    rpc_url = "https://eth-mainnet.nodereal.io/v1/1659dfb40aa24bbb8153a677b98064d7"
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    print(web3.eth.getBalance(account.address))
