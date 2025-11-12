from fastapi import APIRouter, Depends
from app.services import zerodha, strategy
from app import models, schemas
from app.api import deps

router = APIRouter()

@router.post("/place-order")
def place_order(
    order: schemas.Order,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Place a new order.
    """
    kite = zerodha.get_kite()
    order_id = zerodha.place_order(
        kite=kite,
        variety=order.variety,
        exchange=order.exchange,
        tradingsymbol=order.tradingsymbol,
        transaction_type=order.transaction_type,
        quantity=order.quantity,
        product=order.product,
        order_type=order.order_type,
        price=order.price,
        validity=order.validity,
        disclosed_quantity=order.disclosed_quantity,
        trigger_price=order.trigger_price,
        squareoff=order.squareoff,
        stoploss=order.stoploss,
        trailing_stoploss=order.trailing_stoploss,
        tag=order.tag,
    )
    return {"order_id": order_id}

@router.post("/generate-strategy")
def generate_strategy(
    ticker: str,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Generate a trading strategy.
    """
    data = strategy.generate_moving_average_strategy(ticker)
    return data.to_json()
