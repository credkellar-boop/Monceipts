def analyze_transaction(tx_data):
    """
    Basic behavioral forensics for Monceipts.
    Identifies high-velocity movements or new accounts.
    """
    risk_score = 0
    flags = []

    # Example Logic: New account detection
    if tx_data.get('nonce', 0) < 5:
        risk_score += 20
        flags.append("New Account")

    # Example Logic: High-velocity 'Peel Chain' check
    if tx_data.get('value_mon', 0) > 1000:
        risk_score += 10
        flags.append("Large Movement")

    return {
        "risk_score": risk_score,
        "flags": flags,
        "status": "Verified" if risk_score < 50 else "High Risk"
    }
