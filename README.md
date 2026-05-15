## 🧾Monceipts - 💳 Supported Payment Gateways
This project features an omni-channel payment routing system, accepting traditional fiat and Web3 assets across mobile, web, and desktop environments.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Web3.py](https://img.shields.io/badge/Web3.py-Monad_RPC-F37021?style=for-the-badge&logo=ethereum)
![Monad](https://img.shields.io/badge/Monad-Network-0052FF?style=for-the-badge&logo=web3)
![Phantom](https://img.shields.io/badge/Phantom-Wallet-AB9FF2?style=for-the-badge&logo=phantom)
![Dart](https://img.shields.io/badge/Dart-Compiled-0175C2?style=for-the-badge&logo=dart)
![Stripe](https://img.shields.io/badge/Stripe-Fiat_Onramp-008CDD?style=for-the-badge&logo=stripe)

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
