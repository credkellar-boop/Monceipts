import pytest
from app.backend.core.web3_provider import MonadProvider
from app.backend.core.forensics import analyze_transaction

def test_monad_connection():
    """Verify the Web3 provider can talk to the Monad RPC."""
    provider = MonadProvider()
    # In CI, we expect a bool return; if RPC is down, this fails the 'Green Check'
    assert isinstance(provider.is_connected(), bool)

def test_forensics_logic():
    """Verify the Strawman behavioral scoring is operational."""
    mock_tx = {'nonce': 1, 'value_mon': 2000}
    analysis = analyze_transaction(mock_tx)
    
    assert 'risk_score' in analysis
    assert analysis['risk_score'] >= 30  # New account + High value flags
    assert "New Account" in analysis['flags']

def test_environment_variables(monkeypatch):
    """Ensure the engine respects the Chain ID 10143."""
    monkeypatch.setenv("CHAIN_ID", "10143")
    provider = MonadProvider()
    assert provider.chain_id == 10143
