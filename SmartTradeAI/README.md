# SmartTradeAI 🚀

A self-intelligent, secure, and user-friendly algorithmic trading platform integrated with Zerodha Kite and TradingView APIs.

## 🌟 Features

- **AI-Powered Trading Engine**
  - OpenAI GPT-4 integration for market analysis
  - Multi-agent decision support using LangGraph/AutoGen
  - Automated strategy generation and optimization
  - Sentiment analysis from multiple data sources

- **Real-Time Market Data**
  - Live market price updates via WebSocket
  - Portfolio status monitoring
  - P&L tracking
  - Custom technical indicators

- **Security Features**
  - JWT authentication with refresh tokens
  - AES-256 encryption for sensitive data
  - Role-based access control
  - Secure API key management

- **Analytics Dashboard**
  - Interactive charts using D3.js
  - Portfolio performance metrics
  - Risk analysis
  - Backtesting results

- **Automated Notifications**
  - Email alerts via Gmail API
  - Push notifications
  - Telegram bot integration
  - Custom alert configurations

## 🛠 Tech Stack

### Backend
- FastAPI (Python)
- PostgreSQL
- Redis
- Celery
- SQLAlchemy
- WebSocket

### Frontend
- React
- TypeScript
- Tailwind CSS
- D3.js
- Redux Toolkit

### AI/ML
- OpenAI GPT-4
- LangGraph/AutoGen
- PyTorch
- Scikit-learn
- Prophet

### Infrastructure
- Docker
- GitHub Actions
- Nginx

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Redis 7+

### Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/Shuvam-Das/SmartTradeAI.git
   cd SmartTradeAI
   \`\`\`

2. Set up environment variables:
   \`\`\`bash
   cp .env.example .env
   # Edit .env with your configurations
   \`\`\`

3. Start the services:
   \`\`\`bash
   docker-compose up -d
   \`\`\`

4. Initialize the database:
   \`\`\`bash
   docker-compose exec backend alembic upgrade head
   \`\`\`

5. Access the application:
   - Frontend: http://localhost:3000
   - API docs: http://localhost:8000/docs
   - Celery monitoring: http://localhost:5555

## 📝 Configuration

### Required Environment Variables
- \`DATABASE_URL\`: PostgreSQL connection string
- \`REDIS_URL\`: Redis connection string
- \`SECRET_KEY\`: JWT secret key
- \`ZERODHA_API_KEY\`: Zerodha API key
- \`ZERODHA_API_SECRET\`: Zerodha API secret
- \`OPENAI_API_KEY\`: OpenAI API key
- \`NEWS_API_KEY\`: News API key
- \`TELEGRAM_BOT_TOKEN\`: Telegram bot token

## 🔧 Development

### Backend Development
\`\`\`bash
cd backend
python -m venv venv
source venv/bin/activate  # or 'venv\\Scripts\\activate' on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
\`\`\`

### Frontend Development
\`\`\`bash
cd frontend
npm install
npm start
\`\`\`

## 🧪 Testing

### Backend Tests
\`\`\`bash
cd backend
pytest
\`\`\`

### Frontend Tests
\`\`\`bash
cd frontend
npm test
\`\`\`

## 📚 Documentation

- [API Documentation](http://localhost:8000/docs)
- [Architecture Overview](./docs/architecture.md)
- [Development Guide](./docs/development.md)
- [Deployment Guide](./docs/deployment.md)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

## 📄 License

© Shuvam Das 2025 – All Rights Reserved

## 🔐 Security

For security concerns, please email [security@smarttradeai.com](mailto:security@smarttradeai.com)

## 💡 Support

For support, email [support@smarttradeai.com](mailto:support@smarttradeai.com)

## ✨ Acknowledgments

- [Zerodha Kite API](https://kite.trade/)
- [TradingView](https://www.tradingview.com/)
- [OpenAI](https://openai.com/)
- [FastAPI](https://fastapi.tiangolo.com/)