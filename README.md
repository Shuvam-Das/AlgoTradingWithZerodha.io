# AlgoTradingWithZerodha.io

This repository contains the full-stack web application "SmartTradeAI" for automated and agentic algo trading.

## SmartTradeAI

### Objective:
Build a self-intelligent, secure, and user-friendly web platform integrated with Zerodha Kite and TradingView APIs for automated and agentic algo trading. The system will analyze, recommend, and manage investments across equities, intraday, derivatives, ETFs, and mutual funds using real-time and historical data.

### Core Requirements:
1.  Build backend using FastAPI (Python), Redis, Celery, SQLAlchemy, and PostgreSQL.
2.  Frontend with React + Tailwind CSS + D3.js for graph visualization.
3.  Integrate with Zerodha Kite Connect API and TradingView for live data, trading execution, and chart indicators.
4.  Design a self-learning AI engine using:
    -   OpenAI GPT-4, LangGraph, AutoGen, or LightAgent for multi-agent decision support.
    -   yfinance, NSEpy, BeautifulSoup, and NewsAPI for real-time and historical data.
    -   Scikit-learn, Prophet, and PyTorch for prediction and backtesting.
5.  Real-time socket dashboard for live market price, portfolio status, and P&L updates (24×7 backend monitoring).
6.  Implement auto-strategy generation:
    -   Strategize buy/sell timing based on technical, sentiment, and global signals.
    -   Auto-optimize trading strategy and execution workflow.
7.  User authentication:
    -   Secure registration/login with JWT and AES-256 encryption.
    -   Dynamic session tokens and role-based access control.
8.  Notifications:
    -   Auto email using Gmail API and push notifications for alerts, errors, and profit updates.
9.  Security:
    -   Encrypt all user data and API keys.
    -   Add self-healing mechanism to recover failed processes automatically.
10. Agentic AI Core Features:
    -   Portfolio analyzer and screener for any instrument type.
    -   Advanced screener for long-term and short-term investments with “why buy/sell” logic.
    -   Auto-strategy creation for profit booking.
    -   Daily email with performance summary and predictions.
    -   Diagnostic intelligence: show issue alerts in dashboard and email user if a process fails.
11. Optional module:
    -   Create a free AI-powered Telegram bot using python-telegram-bot library that connects to the system for trade instructions, status reports, and live monitoring.

### Data & APIs:
-   For trading data: Kite Connect, NSE, BSE, yfinance, screener.in
-   For global sentiment: News API, Reuters, MarketWatch, company filings, and political data

### Deployment:
1.  Setup Codespace environment with Docker, FastAPI, PostgreSQL, Redis, Node.js, GitHub Actions CI/CD, and environment variables via .env.
2.  Configure GitHub Pages for secure public deployment (frontend) and Render/Fly.io/Heroku for backend service hosting.
3.  Push the entire project structure, scripts, and documentation to GitHub repo.
4.  Include LICENSE (© Shuvam Das 2025 – All Rights Reserved), cookies and caching management, and privacy/security policies.

## Setup and Running the Project

### Prerequisites
- Docker and Docker Compose
- Node.js (version 18 or higher recommended for frontend)
- Python 3.9+ (for backend development outside Docker, if preferred)

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/AlgoTradingWithZerodha.io.git
cd AlgoTradingWithZerodha.io
```

### 2. Navigate to the `SmartTradeAI` directory:
```bash
cd SmartTradeAI
```

### 3. Environment Variables:
Create a `.env` file in the `SmartTradeAI` directory. A basic `.env` file is already provided as `SmartTradeAI/.env`. You can customize it as needed.

### 4. Build and Run with Docker Compose (Recommended):
This will set up and run the PostgreSQL database, Redis, FastAPI backend, and the Nginx-served React frontend.

```bash
docker-compose up --build -d
```
-   The backend API will be available at `http://localhost:8000/api/v1`.
-   The frontend application will be available at `http://localhost:80`.

### 5. Accessing Services:
-   **Backend API Docs (Swagger UI):** `http://localhost:8000/api/v1/docs`
-   **Frontend Application:** `http://localhost:80`

### 6. Database Migrations (using Alembic for backend):
If you make changes to the SQLAlchemy models in the backend, you'll need to generate and apply database migrations.

1.  **Generate a migration:**
    ```bash
    docker-compose exec backend alembic revision --autogenerate -m "Your migration message"
    ```
2.  **Apply migrations:**
    ```bash
    docker-compose exec backend alembic upgrade head
    ```

### 7. Frontend Development (Optional, if not using Docker Compose for frontend):

If you prefer to run the frontend development server separately:

1.  **Navigate to the `frontend` directory:**
    ```bash
    cd frontend
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Run the development server:**
    ```bash
    npm run dev
    ```
    The frontend will typically run on `http://localhost:5173`.

## Project Structure

```
AlgoTradingWithZerodha.io/
├── SmartTradeAI/
│   ├── .env
│   ├── docker-compose.yml
│   ├── README.md
│   ├── backend/
│   │   ├── alembic.ini
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── api/
│   │   │   │   ├── deps.py
│   │   │   │   └── api_v1/
│   │   │   │       └── api.py
│   │   │   ├── core/
│   │   │   │   ├── config.py
│   │   │   │   └── security.py
│   │   │   ├── crud/
│   │   │   │   ├── base.py
│   │   │   │   └── crud_user.py
│   │   │   ├── db/
│   │   │   │   ├── base_class.py
│   │   │   │   ├── base.py
│   │   │   │   ├── init_db.py
│   │   │   │   └── session.py
│   │   │   ├── models/
│   │   │   │   └── user.py
│   │   │   └── schemas/
│   │   │       ├── token.py
│   │   │       └── user.py
│   │   └── alembic/
│   │       ├── env.py
│   │       ├── script.py.mako
│   │       └── versions/ (will be created on first migration)
│   └── frontend/
│       ├── .gitignore
│       ├── Dockerfile
│       ├── eslint.config.js
│       ├── index.html
│       ├── nginx.conf
│       ├── package.json
│       ├── postcss.config.js
│       ├── README.md
│       ├── tailwind.config.js
│       ├── tsconfig.app.json
│       ├── tsconfig.json
│       ├── tsconfig.node.json
│       ├── vite.config.ts
│       └── src/
│           ├── App.css
│           ├── App.jsx
│           ├── index.css
│           └── main.tsx
└── README.md (this file)

```

## License
© Shuvam Das 2025 – All Rights Reserved
