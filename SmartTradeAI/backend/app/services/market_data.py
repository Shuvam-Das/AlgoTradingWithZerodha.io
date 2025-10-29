from typing import Dict, List, Optional
import asyncio
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from app.services.zerodha import zerodha_service
from app.core.socket_manager import socket_manager
from app.utils.logging import logger

class MarketDataService:
    def __init__(self):
        self.subscribed_tokens = set()
        self.last_prices = {}
        self.indicators = {}
        
    async def start_streaming(self, instrument_tokens: List[int], user_id: int):
        """Start streaming market data for given instruments"""
        try:
            # Subscribe to instruments
            for token in instrument_tokens:
                if token not in self.subscribed_tokens:
                    self.subscribed_tokens.add(token)
            
            # Simulate real-time data (replace with actual Zerodha WebSocket)
            while True:
                for token in self.subscribed_tokens:
                    price = self.simulate_price(token)
                    self.last_prices[token] = price
                    
                    # Calculate indicators
                    indicators = self.calculate_indicators(token)
                    
                    # Broadcast to user
                    await socket_manager.broadcast_to_user(
                        user_id,
                        {
                            "event": "marketData",
                            "data": {
                                "token": token,
                                "price": price,
                                "indicators": indicators,
                                "timestamp": datetime.now().isoformat()
                            }
                        }
                    )
                
                await asyncio.sleep(1)  # Update every second
                
        except Exception as e:
            logger.error(f"Error in market data streaming: {str(e)}")
            
    def simulate_price(self, token: int) -> float:
        """Simulate price movement (replace with real data)"""
        last_price = self.last_prices.get(token, 100)
        change = np.random.normal(0, 0.1)  # Random walk
        new_price = last_price * (1 + change)
        return round(new_price, 2)
    
    def calculate_indicators(self, token: int) -> Dict:
        """Calculate technical indicators"""
        if token not in self.indicators:
            self.indicators[token] = []
            
        prices = self.indicators[token]
        current_price = self.last_prices[token]
        prices.append(current_price)
        
        # Keep last 100 prices for calculations
        if len(prices) > 100:
            prices.pop(0)
            
        # Calculate indicators
        df = pd.Series(prices)
        
        return {
            "sma_20": df.rolling(20).mean().iloc[-1] if len(df) >= 20 else None,
            "ema_20": df.ewm(span=20).mean().iloc[-1] if len(df) >= 20 else None,
            "rsi_14": self.calculate_rsi(df, 14) if len(df) >= 14 else None,
            "bollinger_bands": self.calculate_bollinger_bands(df, 20) if len(df) >= 20 else None
        }
    
    def calculate_rsi(self, series: pd.Series, periods: int = 14) -> Optional[float]:
        """Calculate RSI"""
        try:
            delta = series.diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            return round(rsi.iloc[-1], 2)
        except:
            return None
    
    def calculate_bollinger_bands(self, series: pd.Series, periods: int = 20) -> Dict:
        """Calculate Bollinger Bands"""
        try:
            sma = series.rolling(window=periods).mean()
            std = series.rolling(window=periods).std()
            upper_band = sma + (std * 2)
            lower_band = sma - (std * 2)
            return {
                "upper": round(upper_band.iloc[-1], 2),
                "middle": round(sma.iloc[-1], 2),
                "lower": round(lower_band.iloc[-1], 2)
            }
        except:
            return {"upper": None, "middle": None, "lower": None}

    async def get_historical_data(
        self,
        instrument_token: int,
        interval: str = "day",
        days: int = 365
    ) -> List[Dict]:
        """Get historical data with indicators"""
        try:
            to_date = datetime.now()
            from_date = to_date - timedelta(days=days)
            
            data = zerodha_service.get_historical_data(
                instrument_token=instrument_token,
                from_date=from_date.strftime('%Y-%m-%d'),
                to_date=to_date.strftime('%Y-%m-%d'),
                interval=interval
            )
            
            # Convert to pandas DataFrame for calculations
            df = pd.DataFrame(data)
            df['date'] = pd.to_datetime(df['date'])
            
            # Calculate indicators
            df['sma_20'] = df['close'].rolling(20).mean()
            df['ema_20'] = df['close'].ewm(span=20).mean()
            
            # Calculate RSI
            delta = df['close'].diff()
            gain = delta.where(delta > 0, 0).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            df['rsi_14'] = 100 - (100 / (1 + rs))
            
            # Calculate Bollinger Bands
            sma = df['close'].rolling(window=20).mean()
            std = df['close'].rolling(window=20).std()
            df['bb_upper'] = sma + (std * 2)
            df['bb_lower'] = sma - (std * 2)
            
            return df.to_dict('records')
            
        except Exception as e:
            logger.error(f"Error fetching historical data: {str(e)}")
            return []

market_data_service = MarketDataService()