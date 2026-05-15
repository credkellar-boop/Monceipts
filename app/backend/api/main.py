from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from ..core.listener import get_transaction_details
from ..core.forensics import analyze_transaction

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/receipt/{tx_hash}")
async def generate_web_receipt(request: Request, tx_hash: str):
    # 1. Fetch Chain Data
    data = get_transaction_details(tx_hash)
    
    # 2. Run Forensic Analysis
    forensics = analyze_transaction(data)
    
    # 3. Render with Risk Data
    return templates.TemplateResponse("receipt.html", {
        "request": request,
        "ref_code": tx_hash[:10].upper(),
        "mon_amount": f"{data['value_mon']:.8f}",
        "usd_value": f"{float(data['value_mon']) * 0.03:.2f}",
        "risk_status": forensics['status'],
        "risk_score": forensics['risk_score'],
        "flags": forensics['flags']
    })
