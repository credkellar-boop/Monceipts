# 🧾 Monceipts

[![Build Status](https://img.shields.io/github/actions/workflow/status/credkellar-boop/Monceipts/main.yml?branch=main&style=for-the-badge)](https://github.com/credkellar-boop/Monceipts/actions)
[![Monad Devnet](https://img.shields.io/badge/Monad-Chain_10143-836EF1?style=for-the-badge)](https://monad.xyz)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

**Monceipts** is an automated, high-fidelity payment infrastructure designed specifically for the Monad blockchain. It transforms raw transaction hashes into professional, Coinbase-style PDF/PNG receipts with integrated behavioral forensics.


### Payment Flow
1. **Initiation:** Cross-platform Dart client requests payment intent.
2. **Routing:** - *Crypto:* Routes transaction via WalletConnect to Phantom or injected browser wallets.
   - *Fiat:* Routes to Stripe checkout session.
3. **Settlement:** EVM events or Webhooks confirm settlement.
4. **Receipt:** `Monceipts` engine generates and serves the final receipt.
Monceipts/
├── .github/                # CI/CD workflows and repository health
├── app/                    # Main application logic
│   ├── backend/            # Python / FastAPI / Web3.py
│   │   ├── core/           # Blockchain listeners and forensics logic
│   │   ├── api/            # REST endpoints for receipt data
│   │   └── workers/        # Playwright rendering scripts
│   └── frontend/           # Dart / Flutter source code
├── assets/                 # Brand assets and documentation images
├── data/                   # Local database or temporary PNG storage
├── templates/              # HTML/CSS blueprints (The Coinbase style files)
├── tests/                  # Pytest and Dart test suites
├── .env.example            # Template for RPC URLs and API keys
├── docker-compose.yml      # Orchestration for the worker and API
├── README.md               # Main project documentation
└── requirements.txt        # Python dependencies
