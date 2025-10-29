from typing import Dict, List, Optional
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.strategy import Strategy
from app.services.market_data import market_data_service
from app.services.trading import trading_service
from app.utils.logging import logger

class StrategyService:
    def __init__(self):
        self.active_strategies = {}

    async def create_strategy(
        self,
        db: Session,
        user_id: int,
        name: str,
        description: str,
        entry_conditions: Dict,
        exit_conditions: Dict,
        risk_per_trade: float,
        position_size: Optional[float] = None
    ) -> Strategy:
        """Create a new trading strategy"""
        try:
            strategy = Strategy(
                user_id=user_id,
                name=name,
                description=description,
                entry_conditions=entry_conditions,
                exit_conditions=exit_conditions,
                risk_per_trade=risk_per_trade,
                position_size=position_size
            )

            db.add(strategy)
            db.commit()
            db.refresh(strategy)

            return strategy

        except Exception as e:
            logger.error(f"Error creating strategy: {str(e)}")
            raise

    async def backtest_strategy(
        self,
        db: Session,
        strategy_id: int,
        instrument_token: int,
        start_date: datetime,
        end_date: datetime = None
    ) -> Dict:
        """Run strategy backtest"""
        try:
            strategy = db.query(Strategy).filter(Strategy.id == strategy_id).first()
            if not strategy:
                raise ValueError("Strategy not found")

            # Get historical data
            historical_data = await market_data_service.get_historical_data(
                instrument_token=instrument_token,
                interval="day",
                days=(end_date or datetime.now() - start_date).days
            )

            # Convert to DataFrame
            df = pd.DataFrame(historical_data)
            
            # Initialize results
            trades = []
            position = 0
            capital = 100000  # Initial capital
            equity_curve = [capital]

            # Run backtest
            for i in range(len(df)):
                current_bar = df.iloc[i].to_dict()
                
                # Check for exit if in position
                if position != 0:
                    if self.check_exit_conditions(current_bar, strategy.exit_conditions):
                        # Close position
                        exit_price = current_bar['close']
                        pnl = position * (exit_price - entry_price)
                        trades.append({
                            'entry_date': entry_date,
                            'entry_price': entry_price,
                            'exit_date': current_bar['date'],
                            'exit_price': exit_price,
                            'position': position,
                            'pnl': pnl
                        })
                        capital += pnl
                        position = 0

                # Check for entry if not in position
                elif self.check_entry_conditions(current_bar, strategy.entry_conditions):
                    # Open position
                    entry_price = current_bar['close']
                    entry_date = current_bar['date']
                    position = self.calculate_position_size(capital, strategy.risk_per_trade)

                equity_curve.append(capital)

            # Calculate performance metrics
            total_trades = len(trades)
            winning_trades = len([t for t in trades if t['pnl'] > 0])
            total_pnl = sum(t['pnl'] for t in trades)
            max_drawdown = self.calculate_max_drawdown(equity_curve)
            sharpe_ratio = self.calculate_sharpe_ratio(equity_curve)

            # Update strategy with backtest results
            strategy.backtest_results = {
                'total_trades': total_trades,
                'winning_trades': winning_trades,
                'total_pnl': total_pnl,
                'max_drawdown': max_drawdown,
                'sharpe_ratio': sharpe_ratio,
                'equity_curve': equity_curve,
                'trades': trades
            }

            db.add(strategy)
            db.commit()

            return strategy.backtest_results

        except Exception as e:
            logger.error(f"Error running backtest: {str(e)}")
            raise

    def check_entry_conditions(self, bar: Dict, conditions: Dict) -> bool:
        """Check if entry conditions are met"""
        try:
            # Example conditions implementation
            if conditions.get('rsi_oversold'):
                if bar.get('rsi_14', 100) > 30:
                    return False
                    
            if conditions.get('sma_crossover'):
                if bar.get('sma_20', 0) < bar.get('close', 0):
                    return False

            if conditions.get('bollinger_bounce'):
                bb = bar.get('bollinger_bands', {})
                if bar.get('close', 0) > bb.get('lower', 0):
                    return False

            return True

        except Exception as e:
            logger.error(f"Error checking entry conditions: {str(e)}")
            return False

    def check_exit_conditions(self, bar: Dict, conditions: Dict) -> bool:
        """Check if exit conditions are met"""
        try:
            # Example conditions implementation
            if conditions.get('rsi_overbought'):
                if bar.get('rsi_14', 0) < 70:
                    return False
                    
            if conditions.get('sma_crossunder'):
                if bar.get('sma_20', 0) > bar.get('close', 0):
                    return False

            if conditions.get('bollinger_breakdown'):
                bb = bar.get('bollinger_bands', {})
                if bar.get('close', 0) < bb.get('upper', 0):
                    return False

            return True

        except Exception as e:
            logger.error(f"Error checking exit conditions: {str(e)}")
            return False

    def calculate_position_size(self, capital: float, risk_per_trade: float) -> int:
        """Calculate position size based on risk parameters"""
        return int((capital * risk_per_trade) / 100)

    def calculate_max_drawdown(self, equity_curve: List[float]) -> float:
        """Calculate maximum drawdown"""
        peaks = pd.Series(equity_curve).expanding(min_periods=1).max()
        drawdowns = pd.Series(equity_curve) / peaks - 1
        return float(drawdowns.min() * 100)

    def calculate_sharpe_ratio(self, equity_curve: List[float], risk_free_rate: float = 0.02) -> float:
        """Calculate Sharpe ratio"""
        returns = pd.Series(equity_curve).pct_change().dropna()
        excess_returns = returns - risk_free_rate / 252  # Daily risk-free rate
        return float(np.sqrt(252) * excess_returns.mean() / excess_returns.std())

strategy_service = StrategyService()