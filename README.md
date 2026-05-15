# 🧾 Monceipts

[![Build Status](https://img.shields.io/github/actions/workflow/status/credkellar-boop/Monceipts/main.yml?branch=main&style=for-the-badge)](https://github.com/credkellar-boop/Monceipts/actions)
[![Monad Devnet](https://img.shields.io/badge/Monad-Chain_10143-836EF1?style=for-the-badge)](https://monad.xyz)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Dart](https://img.shields.io/badge/Dart-Compiled-0175C2?style=for-the-badge&logo=dart&logoColor=white)](https://dart.dev)

**Monceipts** is an automated, high-fidelity payment infrastructure designed specifically for the Monad blockchain. It transforms raw transaction hashes into professional, Coinbase-style PDF/PNG receipts with integrated behavioral forensics and risk scoring.

---

## 🚀 Payment Flow

1. **Initiation**: Cross-platform Dart client requests payment intent.
2. **Routing**: 
   - **Crypto**: Routes transaction via WalletConnect to Phantom or injected browser wallets.
   - **Fiat**: Routes to Stripe checkout session.
3. **Settlement**: EVM events (Chain 10143) or Webhooks confirm settlement.
4. **Receipt**: Monceipts engine generates and serves the final receipt via Playwright rendering.

---

## 📁 Project Structure

```text
Monceipts/
├── .github/workflows/      # CI/CD: Backend tests, Security scans, Main CI
├── app/                    # Main application logic
│   ├── backend/            # Python / FastAPI / Web3.py
│   │   ├── api/            # REST endpoints, Security middleware, Routing
│   │   ├── core/           # Web3 listeners, Forensics engine, Models
│   │   └── workers/        # Playwright rendering scripts (renderer.py)
│   └── frontend/           # Dart / Flutter source code
├── assets/                 # Brand assets and documentation images
├── data/                   # Redis cache and temporary receipt storage
├── templates/              # Jinja2 HTML/CSS blueprints (Coinbase style)
├── Dockerfile              # Containerization for Playwright/Python
├── docker-compose.yml      # Orchestration with Redis and PostgreSQL
└── merge_repos.sh          # Monorepo consolidation script
