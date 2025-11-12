from typing import Optional
from pydantic import BaseModel

class Order(BaseModel):
    variety: str
    exchange: str
    tradingsymbol: str
    transaction_type: str
    quantity: int
    product: str
    order_type: str
    price: Optional[float] = None
    validity: Optional[str] = None
    disclosed_quantity: Optional[int] = None
    trigger_price: Optional[float] = None
    squareoff: Optional[float] = None
    stoploss: Optional[float] = None
    trailing_stoploss: Optional[float] = None
    tag: Optional[str] = None
