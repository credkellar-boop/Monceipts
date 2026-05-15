import os
from web3 import Web3

# Monad Devnet Configuration
RPC_URL = "https://rpc-devnet.monad.xyz"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

def get_transaction_details(tx_hash):
    tx = w3.eth.get_transaction(tx_hash)
    receipt = w3.eth.get_transaction_receipt(tx_hash)
    
    return {
        "hash": tx_hash,
        "from": tx['from'],
        "value_mon": w3.from_wei(tx['value'], 'ether'),
        "status": "Success" if receipt.status == 1 else "Failed",
        "block": tx['blockNumber']
    }
