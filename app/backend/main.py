import asyncio
import uvicorn
from multiprocessing import Process
from .core.listener import watch_payments
from .api.main import app

def run_api():
    """Starts the FastAPI server for receipt delivery."""
    uvicorn.run(app, host="0.0.0.0", port=8000)

def run_watcher():
    """Starts the background worker to listen for MON transactions."""
    print("🚀 Starting Monad Blockchain Watchdog...")
    watch_payments()

if __name__ == "__main__":
    # Create two processes: one for the API and one for the Blockchain Watcher
    api_process = Process(target=run_api)
    watcher_process = Process(target=run_watcher)

    api_process.start()
    watcher_process.start()

    api_process.join()
    watcher_process.join()
from fastapi.responses import FileResponse
import os

@app.get("/download/{tx_hash}")
async def download_receipt(tx_hash: str):
    file_path = f"data/receipts/{tx_hash}.png"
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path, 
            filename=f"Monceipt_{tx_hash[:8]}.png", 
            media_type='image/png'
        )
    return {"error": "Receipt not found. Has it been rendered yet?"}
