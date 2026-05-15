import asyncio
from playwright.async_api import async_playwright
import os

async def capture_receipt(tx_hash):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Point to your local FastAPI endpoint
        url = f"http://localhost:8000/receipt/{tx_hash}"
        await page.goto(url)
        
        # Ensure the 'data' directory exists
        os.makedirs("data/receipts", exist_ok=True)
        
        # Capture the specific receipt container
        receipt_path = f"data/receipts/{tx_hash}.png"
        await page.locator(".receipt-card").screenshot(path=receipt_path)
        
        await browser.close()
        print(f"Receipt generated: {receipt_path}")
        return receipt_path

if __name__ == "__main__":
    # Test with a dummy hash
    asyncio.run(capture_receipt("AA364E8T54"))
