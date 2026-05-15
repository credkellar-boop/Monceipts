from fastapi import APIRouter
from ..core.web3_provider import MonadProvider
import shutil

router = APIRouter()
monad = MonadProvider()

@router.get("/status")
async def get_system_status():
    return {
        "blockchain": "Connected" if monad.is_connected() else "Disconnected",
        "network": "Monad Devnet (10143)",
        "render_engine": "Ready" if shutil.which("chromium") else "Missing Dependencies",
        "storage_disk_usage": shutil.disk_usage("/").free // (2**30), # GB free
        "version": "1.0.4-stable"
    }
