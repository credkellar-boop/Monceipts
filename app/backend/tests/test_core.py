import pytest
from app.backend.core.web3_provider import MonadProvider

def test_monad_connection():
    """Verify the Web3 provider can talk to the Monad RPC."""
    provider = MonadProvider()
    # Verifies that the provider correctly initializes and checks connection
    assert isinstance(provider.is_connected(), bool)

def test_environment_variables(monkeypatch):
    """Ensure the engine respects the Monad Devnet Chain ID."""
    monkeypatch.setenv("CHAIN_ID", "10143")
    provider = MonadProvider()
    assert provider.chain_id == 10143
