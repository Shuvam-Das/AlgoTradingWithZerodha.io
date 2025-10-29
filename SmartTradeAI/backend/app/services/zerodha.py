from typing import Dict, List, Optional
from kiteconnect import KiteConnect
from app.core.config import settings
from app.utils.logging import logger

class ZerodhaService:
    def __init__(self, api_key: str, api_secret: str, access_token: Optional[str] = None):
        self.api_key = api_key
        self.api_secret = api_secret
        self.kite = KiteConnect(api_key=api_key)
        if access_token:
            self.kite.set_access_token(access_token)

    def generate_login_url(self) -> str:
        """Generate the Zerodha login URL for OAuth"""
        return self.kite.login_url()

    def generate_session(self, request_token: str) -> Dict:
        """Exchange request token for access token"""
        try:
            data = self.kite.generate_session(
                request_token=request_token,
                api_secret=self.api_secret
            )
            return data
        except Exception as e:
            logger.error(f"Error generating Zerodha session: {str(e)}")
            raise

    def get_positions(self) -> List[Dict]:
        """Get current positions"""
        try:
            return self.kite.positions()
        except Exception as e:
            logger.error(f"Error fetching positions: {str(e)}")
            return []

    def get_holdings(self) -> List[Dict]:
        """Get current holdings"""
        try:
            return self.kite.holdings()
        except Exception as e:
            logger.error(f"Error fetching holdings: {str(e)}")
            return []

    def place_order(
        self,
        tradingsymbol: str,
        exchange: str,
        transaction_type: str,
        quantity: int,
        product: str,
        order_type: str,
        price: float = None,
        trigger_price: float = None
    ) -> str:
        """Place an order"""
        try:
            order_id = self.kite.place_order(
                variety=self.kite.VARIETY_REGULAR,
                exchange=exchange,
                tradingsymbol=tradingsymbol,
                transaction_type=transaction_type,
                quantity=quantity,
                product=product,
                order_type=order_type,
                price=price,
                trigger_price=trigger_price
            )
            return order_id
        except Exception as e:
            logger.error(f"Error placing order: {str(e)}")
            raise

    def modify_order(
        self,
        order_id: str,
        quantity: int = None,
        price: float = None,
        trigger_price: float = None,
        order_type: str = None
    ) -> bool:
        """Modify an existing order"""
        try:
            self.kite.modify_order(
                variety=self.kite.VARIETY_REGULAR,
                order_id=order_id,
                quantity=quantity,
                price=price,
                trigger_price=trigger_price,
                order_type=order_type
            )
            return True
        except Exception as e:
            logger.error(f"Error modifying order: {str(e)}")
            return False

    def cancel_order(self, order_id: str) -> bool:
        """Cancel an order"""
        try:
            self.kite.cancel_order(
                variety=self.kite.VARIETY_REGULAR,
                order_id=order_id
            )
            return True
        except Exception as e:
            logger.error(f"Error cancelling order: {str(e)}")
            return False

    def get_order_history(self, order_id: str = None) -> List[Dict]:
        """Get order history"""
        try:
            return self.kite.orders(order_id)
        except Exception as e:
            logger.error(f"Error fetching order history: {str(e)}")
            return []

    def get_margins(self) -> Dict:
        """Get available margins"""
        try:
            return self.kite.margins()
        except Exception as e:
            logger.error(f"Error fetching margins: {str(e)}")
            return {}

    def get_historical_data(
        self,
        instrument_token: int,
        from_date: str,
        to_date: str,
        interval: str,
        continuous: bool = False,
        oi: bool = False
    ) -> List[Dict]:
        """Get historical data"""
        try:
            return self.kite.historical_data(
                instrument_token=instrument_token,
                from_date=from_date,
                to_date=to_date,
                interval=interval,
                continuous=continuous,
                oi=oi
            )
        except Exception as e:
            logger.error(f"Error fetching historical data: {str(e)}")
            return []

zerodha_service = ZerodhaService(
    api_key=settings.ZERODHA_API_KEY,
    api_secret=settings.ZERODHA_API_SECRET
)