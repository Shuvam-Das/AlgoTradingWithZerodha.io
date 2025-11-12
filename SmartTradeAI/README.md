# SmartTradeAI

## Objective:
Build a self-intelligent, secure, and user-friendly web platform integrated with Zerodha Kite and TradingView APIs for automated and agentic algo trading. The system will analyze, recommend, and manage investments across equities, intraday, derivatives, ETFs, and mutual funds using real-time and historical data.

## Core Requirements:
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

## Data & APIs:
-   For trading data: Kite Connect, NSE, BSE, yfinance, screener.in
-   For global sentiment: News API, Reuters, MarketWatch, company filings, and political data

## Deployment:
1.  Setup Codespace environment with Docker, FastAPI, PostgreSQL, Redis, Node.js, GitHub Actions CI/CD, and environment variables via .env.
2.  Configure GitHub Pages for secure public deployment (frontend) and Render/Fly.io/Heroku for backend service hosting.
3.  Push the entire project structure, scripts, and documentation to GitHub repo.
4.  Include LICENSE (© Shuvam Das 2025 – All Rights Reserved), cookies and caching management, and privacy/security policies.

## Setup and Running the Project

### Prerequisites
- Docker and Docker Compose
- Python 3.9+

### Backend Setup

1.  **Navigate to the `SmartTradeAI` directory:**
    ```bash
    cd SmartTradeAI
    ```

2.  **Create a `.env` file:**
    Copy the `.env.example` (if it existed, but we just created it) or create a new `.env` file in the `SmartTradeAI` directory and fill in the environment variables. A basic `.env` file is already created for you.

3.  **Build and run the Docker containers:**
    ```bash
    docker-compose up --build
    ```
    This will start the PostgreSQL database, Redis, and the FastAPI backend.

4.  **Access the backend API:**
    The FastAPI application will be running at `http://localhost:8000`. You can access the API documentation (Swagger UI) at `http://localhost:8000/api/v1/docs`.

### Database Migrations (using Alembic)

1.  **Initialize Alembic (if not already done):**
    ```bash
    docker-compose exec backend alembic init alembic
    ```
    *(Note: This step has been handled by the agent during setup)*

2.  **Generate a migration:**
    After making changes to your SQLAlchemy models, generate a new migration script:
    ```bash
    docker-compose exec backend alembic revision --autogenerate -m "Add initial models"
    ```

3.  **Apply migrations:**
    ```bash
    docker-compose exec backend alembic upgrade head
    ```

### Frontend Setup (To be implemented)

Instructions for setting up and running the React frontend will be added here.

## Project Structure

```
SmartTradeAI/
├── .env
├── docker-compose.yml
├── README.md
├── backend/
│   ├── alembic.ini
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── deps.py
│   │   │   └── api_v1/
│   │   │       └── api.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── crud/
│   │   │   ├── base.py
│   │   │   └── crud_user.py
│   │   ├── db/
│   │   │   ├── base_class.py
│   │   │   ├── base.py
│   │   │   ├── init_db.py
│   │   │   └── session.py
│   │   ├── models/
│   │   │   └── user.py
│   │   └── schemas/
│   │       ├── token.py
│   │       └── user.py
│   └── alembic/
│       ├── env.py
│       └── script.py.mako
└── frontend/
    ├── ... (React app files)
```

## License
© Shuvam Das 2025 – All Rights Reserved
