import argparse
import yfinance as yf

DEFAULT_STOCKS = ["AAPL", "MSFT", "TSLA"]  # Default stocks to monitor


def get_current_stock_prices(stocks=DEFAULT_STOCKS):
    """
    Retrieve and display the current stock prices for the given stocks.

    Parameters:
        stocks (list of str): A list of stock symbols to monitor.

    Returns:
        dict: A dictionary mapping stock symbols to their current prices.
    """
    try:
        tickers = yf.Tickers(stocks)
        data = tickers.history(period="1d", interval="1m")
        prices = data['Close'].values.tolist()
        stock_prices = {}
        for stock, price in zip(stocks, prices):
            stock_prices[stock] = price
            print(f"{stock}: ${price}")
        return stock_prices
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve current stock prices.")
    parser.add_argument("-s", "--stocks", nargs="+", help="List of stocks to monitor.")
    args = parser.parse_args()

    # Retrieve and display the current stock prices
    if args.stocks:
        get_current_stock_prices(args.stocks)
    else:
        get_current_stock_prices()
