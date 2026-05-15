from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from ..core.listener import get_transaction_details

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/receipt/{tx_hash}")
async def generate_web_receipt(request: Request, tx_hash: str):
    data = get_transaction_details(tx_hash)
    # Mapping data to the Coinbase blueprint placeholders
    return templates.TemplateResponse("receipt.html", {
        "request": request,
        "ref_code": tx_hash[:10].upper(),
        "mon_amount": f"{data['value_mon']:.8f}",
        "usd_value": f"{float(data['value_mon']) * 0.03:.2f}", # Mock price
        "date": "2026/05/14"
    })
