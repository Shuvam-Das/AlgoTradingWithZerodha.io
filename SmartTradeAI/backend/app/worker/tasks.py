from app.core.celery_app import celery_app
from app.services import market_data, strategy
from app.core.config import settings
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@celery_app.task(acks_late=True)
def get_stock_data_task(ticker: str, start_date: str, end_date: str):
    """
    Celery task to get stock data.
    """
    logger.info(f"Getting stock data for {ticker}")
    data = market_data.get_stock_data(ticker, start_date, end_date)
    return data.to_json()

@celery_app.task(acks_late=True)
def run_sma_strategy_task(ticker: str, start_date: str, end_date: str, short_window: int = 20, long_window: int = 50):
    """
    Celery task to run SMA strategy.
    """
    logger.info(f"Running SMA strategy for {ticker}")
    data = strategy.get_sma_strategy(ticker, start_date, end_date, short_window, long_window)
    return data.to_json()
