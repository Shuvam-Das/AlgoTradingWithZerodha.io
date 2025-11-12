from fastapi import APIRouter, Depends
from app.worker import tasks
from app import models
from app.api import deps

router = APIRouter()

@router.post("/run-sma-strategy", status_code=201)
def run_sma_strategy(
    ticker: str,
    start_date: str,
    end_date: str,
    short_window: int = 20,
    long_window: int = 50,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Run SMA strategy task.
    """
    tasks.run_sma_strategy_task.delay(ticker, start_date, end_date, short_window, long_window)
    return {"msg": "SMA strategy task has been triggered"}

@router.post("/get-stock-data", status_code=201)
def get_stock_data(
    ticker: str,
    start_date: str,
    end_date: str,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    """
    Get stock data task.
    """
    tasks.get_stock_data_task.delay(ticker, start_date, end_date)
    return {"msg": "Get stock data task has been triggered"}
