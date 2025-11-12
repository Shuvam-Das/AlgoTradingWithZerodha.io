from kiteconnect import KiteConnect
from app.core.config import settings

def get_kite():
    """
    Initialize KiteConnect
    """
    kite = KiteConnect(api_key=settings.KITE_API_KEY)
    kite.set_access_token(settings.KITE_ACCESS_TOKEN)
    return kite

def get_profile(kite: KiteConnect):
    """
    Get user profile
    """
    return kite.profile()

def get_holdings(kite: KiteConnect):
    """
    Get holdings
    """
    return kite.holdings()

def get_positions(kite: KiteConnect):
    """
    Get positions
    """
    return kite.positions()

def place_order(kite: KiteConnect, variety: str, exchange: str, tradingsymbol: str, transaction_type: str, quantity: int, product: str, order_type: str, price: float = None, validity: str = None, disclosed_quantity: int = None, trigger_price: float = None, squareoff: float = None, stoploss: float = None, trailing_stoploss: float = None, tag: str = None):
    """
    Place an order
    """
    try:
        order_id = kite.place_order(
            variety=variety,
            exchange=exchange,
            tradingsymbol=tradingsymbol,
            transaction_type=transaction_type,
            quantity=quantity,
            product=product,
            order_type=order_type,
            price=price,
            validity=validity,
            disclosed_quantity=disclosed_quantity,
            trigger_price=trigger_price,
            squareoff=squareoff,
            stoploss=stoploss,
            trailing_stoploss=trailing_stoploss,
            tag=tag
        )
        return order_id
    except Exception as e:
        raise e
