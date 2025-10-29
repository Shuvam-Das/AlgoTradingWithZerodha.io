from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db.base_class import Base

class TradeType(enum.Enum):
    BUY = "BUY"
    SELL = "SELL"

class TradeStatus(enum.Enum):
    PENDING = "PENDING"
    EXECUTED = "EXECUTED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"))
    strategy_id = Column(Integer, ForeignKey("strategies.id"), nullable=True)
    
    symbol = Column(String, nullable=False)
    trade_type = Column(Enum(TradeType), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(Enum(TradeStatus), default=TradeStatus.PENDING)
    
    order_id = Column(String, nullable=True)  # Zerodha order ID
    exchange = Column(String, nullable=False)
    product = Column(String, nullable=False)  # NRML, MIS, CNC
    
    entry_time = Column(DateTime, default=datetime.utcnow)
    execution_time = Column(DateTime, nullable=True)
    
    stop_loss = Column(Float, nullable=True)
    target = Column(Float, nullable=True)
    trailing_sl = Column(Float, nullable=True)
    
    pnl = Column(Float, nullable=True)
    charges = Column(Float, default=0.0)
    
    notes = Column(String, nullable=True)
    meta_data = Column(JSON, nullable=True)  # For additional trade information
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="trades")
    portfolio = relationship("Portfolio", back_populates="trades")
    strategy = relationship("Strategy", back_populates="trades")