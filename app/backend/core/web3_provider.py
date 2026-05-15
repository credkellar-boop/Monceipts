import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

class MonadProvider:
    def __init__(self):
        self.rpc_url = os.getenv("MONAD_RPC_URL", "https://rpc-devnet.monad.xyz")
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        self.chain_id = int(os.getenv("CHAIN_ID", 10143))

    def is_connected(self):
        return self.w3.is_connected()

    def get_transaction(self, tx_hash):
        """Fetches full transaction data for the receipt."""
        try:
            tx = self.w3.eth.get_transaction(tx_hash)
            receipt = self.w3.eth.get_transaction_receipt(tx_hash)
            
            return {
                "hash": tx_hash.hex() if isinstance(tx_hash, bytes) else tx_hash,
                "from": tx['from'],
                "to": tx['to'],
                "value": self.w3.from_wei(tx['value'], 'ether'),
                "gas_used": receipt['gasUsed'],
                "status": "Success" if receipt['status'] == 1 else "Failed",
                "block": tx['blockNumber'],
                "nonce": tx['nonce']
            }
        except Exception as e:
            print(f"Error fetching TX {tx_hash}: {e}")
            return None

    def monitor_blocks(self, callback_func):
        """Infinite loop to listen for new blocks and process transactions."""
        last_block = self.w3.eth.block_number
        print(f"Monitoring Monad starting from block {last_block}...")
        
        while True:
            current_block = self.w3.eth.block_number
            if current_block > last_block:
                block = self.w3.eth.get_block(current_block, full_transactions=True)
                for tx in block.transactions:
                    callback_func(tx)
                last_block = current_block
