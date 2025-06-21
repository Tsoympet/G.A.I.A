import yfinance as yf
import pandas as pd

class StockAnalyzer:
    def __init__(self, symbol):
        self.symbol = symbol
        self.stock = yf.Ticker(symbol)

    def get_summary(self):
        info = self.stock.info
        return {
            'symbol': self.symbol,
            'name': info.get('shortName'),
            'sector': info.get('sector'),
            'marketCap': info.get('marketCap'),
            'price': info.get('regularMarketPrice'),
            'peRatio': info.get('trailingPE'),
            'dividendYield': info.get('dividendYield')
        }

    def get_price_history(self, period='6mo', interval='1d'):
        hist = self.stock.history(period=period, interval=interval)
        return hist

    def calculate_moving_average(self, window=20):
        hist = self.get_price_history()
        hist['MA'] = hist['Close'].rolling(window=window).mean()
        return hist[['Close', 'MA']]
