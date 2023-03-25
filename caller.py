import argparse
from typing import List, Dict, Any

import yfinance as yf

DEFAULT_STOCKS = ["AAPL", "MSFT", "TSLA"]  # Default stocks to monitor


def get_current_stock_prices(stocks: List[str] = None) -> Dict[str, Any]:
    """
    Retrieve and display the current stock prices for the given stocks.

    Parameters:
        stocks (list of str): A list of stock symbols to monitor.

    Returns:
        dict: A dictionary mapping stock symbols to their current prices.
    """
    if stocks is None:
        stocks = DEFAULT_STOCKS
    try:
        if len(stocks) == 1:
            ticker = yf.Ticker(stocks[0])
            data = ticker.history(period="1d", interval="1m")
            prices = data['Close'].values.tolist()
            stock_prices = {}
        else:
            tickers = yf.Tickers(stocks)
            data = tickers.history(period="1d", interval="1m")
            prices = data['Close'].values.tolist()
            stock_prices = {}
        for stock, price in zip(stocks, prices):
            stock_prices[stock] = price
            print(f"{stock}: ${price:}")
        return stock_prices
    except ValueError as e:
        print(f"Invalid stock symbol: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve current stock prices.")
    parser.add_argument("-s", "--stocks", nargs="+", help="List of stocks to monitor.")
    parser.add_argument("-d", "--default_stocks", nargs="+", help="Set the default stocks to monitor.")
    args = parser.parse_args()

    # Set the default stocks if provided
    if args.default_stocks:
        DEFAULT_STOCKS = args.default_stocks

    # Determine which stocks to monitor
    if args.stocks:
        query = args.stocks
    else:
        query = DEFAULT_STOCKS

    # Retrieve and display the current stock prices
    get_current_stock_prices(query)
