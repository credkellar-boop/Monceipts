# Centralizing service logic for the Monorepo merger
SERVICES = {
    "monceipts": "Receipt Generation Engine",
    "strawman": "OSINT & Identity Forensics",
    "top_winners": "Arbitrage Betting Tracking",
    "crypto_raid": "Automated Engagement Bot"
}

def route_transaction(tx_type):
    """
    Determines which service logic to apply based on incoming data.
    """
    if tx_type == "bet":
        return SERVICES["top_winners"]
    elif tx_type == "transfer":
        return SERVICES["monceipts"]
    else:
        return SERVICES["strawman"]
