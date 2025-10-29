from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class Strategy(Base):
    __tablename__ = "strategies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    
    # Strategy Parameters
    entry_conditions = Column(JSON, nullable=False)  # JSON containing entry rules
    exit_conditions = Column(JSON, nullable=False)   # JSON containing exit rules
    risk_per_trade = Column(Float, default=1.0)     # Percentage of portfolio
    position_size = Column(Float, nullable=True)     # Fixed position size if any
    
    # Performance Metrics
    total_trades = Column(Integer, default=0)
    winning_trades = Column(Integer, default=0)
    losing_trades = Column(Integer, default=0)
    total_pnl = Column(Float, default=0.0)
    max_drawdown = Column(Float, default=0.0)
    sharpe_ratio = Column(Float, nullable=True)
    
    # Strategy Status
    is_active = Column(Boolean, default=True)
    is_automated = Column(Boolean, default=False)
    last_execution = Column(DateTime, nullable=True)
    
    # Backtest Results
    backtest_results = Column(JSON, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="strategies")
    trades = relationship("Trade", back_populates="strategy")