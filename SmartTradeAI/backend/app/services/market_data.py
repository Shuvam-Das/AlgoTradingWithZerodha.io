import yfinance as yf
import nsepy
from datetime import date
from newsapi import NewsApiClient
from app.core.config import settings

def get_stock_data(ticker: str, start_date: str, end_date: str):
    """
    Get stock data from yfinance
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def get_nse_data(symbol: str, start_date: date, end_date: date):
    """
    Get stock data from nsepy
    """
    data = nsepy.get_history(symbol=symbol, start=start_date, end=end_date)
    return data

def get_top_news():
    """
    Get top news from NewsAPI
    """
    newsapi = NewsApiClient(api_key=settings.NEWS_API_KEY)
    top_headlines = newsapi.get_top_headlines(language='en', country='in')
    return top_headlines
