from fastapi import APIRouter

api_router = APIRouter()

# Import and include all API routes
from app.api.v1.endpoints import (
    auth,
    users,
    trades,
    portfolio,
    analytics,
    strategies,
    notifications
)

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(trades.router, prefix="/trades", tags=["Trades"])
api_router.include_router(portfolio.router, prefix="/portfolio", tags=["Portfolio"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
api_router.include_router(strategies.router, prefix="/strategies", tags=["Trading Strategies"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])