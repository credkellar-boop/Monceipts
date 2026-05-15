from enum import Enum

class ProjectType(Enum):
    MONCEIPTS = "Standard Payment"
    STRAWMAN = "Identity Audit"
    TOP_WINNERS = "Arbitrage Win"
    CRYPTO_RAID = "Bot Engagement"

def get_receipt_metadata(project_type: ProjectType, tx_data: dict):
    """Customizes receipt data based on the specific merged project."""
    base_data = {"tx_hash": tx_data['hash'], "amount": tx_data['value']}
    
    if project_type == ProjectType.TOP_WINNERS:
        base_data["extra_label"] = "Arbitrage Profit"
        base_data["extra_value"] = f"+{float(tx_data['value']) * 0.15:.4f} MON"
    elif project_type == ProjectType.STRAWMAN:
        base_data["extra_label"] = "Forensic Trust Score"
        base_data["extra_value"] = "98/100 (Safe)"
        
    return base_data
