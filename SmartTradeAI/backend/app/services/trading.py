from typing import Dict, List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from app.services.zerodha import zerodha_service
from app.models.trade import Trade, TradeType, TradeStatus
from app.models.portfolio import Portfolio
from app.utils.logging import logger

class TradingService:
    def __init__(self):
        self.order_cache = {}

    async def place_order(
        self,
        db: Session,
        user_id: int,
        portfolio_id: int,
        symbol: str,
        trade_type: TradeType,
        quantity: int,
        price: float,
        order_type: str = "LIMIT",
        product: str = "CNC",
        stop_loss: Optional[float] = None,
        target: Optional[float] = None,
        strategy_id: Optional[int] = None
    ) -> Trade:
        """Place a new trade order"""
        try:
            # Calculate total amount
            total_amount = quantity * price

            # Create trade record
            trade = Trade(
                user_id=user_id,
                portfolio_id=portfolio_id,
                strategy_id=strategy_id,
                symbol=symbol,
                trade_type=trade_type,
                quantity=quantity,
                price=price,
                total_amount=total_amount,
                product=product,
                stop_loss=stop_loss,
                target=target,
                exchange="NSE"  # Default to NSE, make configurable if needed
            )

            # Place order with Zerodha
            order_id = zerodha_service.place_order(
                tradingsymbol=symbol,
                exchange="NSE",
                transaction_type="BUY" if trade_type == TradeType.BUY else "SELL",
                quantity=quantity,
                product=product,
                order_type=order_type,
                price=price
            )

            trade.order_id = order_id
            trade.status = TradeStatus.EXECUTED
            trade.execution_time = datetime.utcnow()

            # Save to database
            db.add(trade)
            db.commit()
            db.refresh(trade)

            # Update portfolio
            await self.update_portfolio(db, portfolio_id)

            return trade

        except Exception as e:
            logger.error(f"Error placing order: {str(e)}")
            if 'trade' in locals():
                trade.status = TradeStatus.FAILED
                db.add(trade)
                db.commit()
            raise

    async def update_portfolio(self, db: Session, portfolio_id: int):
        """Update portfolio with current positions and calculations"""
        try:
            portfolio = db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()
            if not portfolio:
                return

            # Get current positions from Zerodha
            positions = zerodha_service.get_positions()
            holdings = zerodha_service.get_holdings()

            # Calculate total value and P&L
            total_value = 0
            unrealized_pnl = 0
            realized_pnl = 0

            for position in positions:
                total_value += position.get('value', 0)
                unrealized_pnl += position.get('unrealized_pnl', 0)
                realized_pnl += position.get('realized_pnl', 0)

            for holding in holdings:
                total_value += holding.get('value', 0)
                unrealized_pnl += holding.get('unrealized_pnl', 0)

            # Update portfolio
            portfolio.total_value = total_value
            portfolio.unrealized_pnl = unrealized_pnl
            portfolio.realized_pnl = realized_pnl

            # Calculate risk metrics
            portfolio.risk_metrics = self.calculate_risk_metrics(positions + holdings)

            db.add(portfolio)
            db.commit()

        except Exception as e:
            logger.error(f"Error updating portfolio: {str(e)}")
            raise

    def calculate_risk_metrics(self, positions: List[Dict]) -> Dict:
        """Calculate risk metrics for the portfolio"""
        try:
            total_exposure = sum(abs(p.get('value', 0)) for p in positions)
            position_exposures = [abs(p.get('value', 0)) for p in positions]
            
            return {
                "total_exposure": total_exposure,
                "largest_position": max(position_exposures) if position_exposures else 0,
                "position_count": len(positions),
                "concentration": max(position_exposures) / total_exposure if total_exposure else 0
            }
        except Exception as e:
            logger.error(f"Error calculating risk metrics: {str(e)}")
            return {}

    async def close_position(
        self,
        db: Session,
        user_id: int,
        portfolio_id: int,
        trade_id: int
    ) -> bool:
        """Close an existing position"""
        try:
            # Get the original trade
            trade = db.query(Trade).filter(
                Trade.id == trade_id,
                Trade.user_id == user_id
            ).first()

            if not trade:
                raise ValueError("Trade not found")

            # Place opposite order
            opposite_type = TradeType.SELL if trade.trade_type == TradeType.BUY else TradeType.BUY
            
            await self.place_order(
                db=db,
                user_id=user_id,
                portfolio_id=portfolio_id,
                symbol=trade.symbol,
                trade_type=opposite_type,
                quantity=trade.quantity,
                price=zerodha_service.kite.ltp(trade.symbol)['ltp'],
                product=trade.product
            )

            return True

        except Exception as e:
            logger.error(f"Error closing position: {str(e)}")
            return False

trading_service = TradingService()