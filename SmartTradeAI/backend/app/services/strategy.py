import pandas as pd
from app.services import market_data
from app.services import zerodha
from app.core.config import settings
import openai

openai.api_key = settings.OPENAI_API_KEY

def get_sma_strategy(ticker: str, start_date: str, end_date: str, short_window: int = 20, long_window: int = 50):
    """
    Simple Moving Average Crossover Strategy
    """
    data = market_data.get_stock_data(ticker, start_date, end_date)
    data['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    data['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    data['signal'] = 0.0
    data['signal'][short_window:] = pd.where(data['short_mavg'][short_window:] > data['long_mavg'][short_window:], 1.0, 0.0)
    data['positions'] = data['signal'].diff()
    return data

def get_sentiment_analysis(text: str):
    """
    Get sentiment analysis from OpenAI
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text and return 'positive', 'negative', or 'neutral'.\n\nText: {text}\n\nSentiment:",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text.strip().lower()
