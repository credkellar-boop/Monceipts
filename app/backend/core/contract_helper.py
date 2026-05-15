import json

def load_contract(w3, address, abi_path):
    with open(abi_path, 'r') as f:
        abi = json.load(f)
    return w3.eth.contract(address=address, abi=abi)

# Example usage for a 'Payment' event
def decode_payment_event(contract, tx_receipt):
    # This parses log data into readable Python dictionaries
    return contract.events.PaymentReceived().process_receipt(tx_receipt)
