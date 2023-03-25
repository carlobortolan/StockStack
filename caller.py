import argparse
import yfinance as yf

DEFAULT_STOCKS = ["AAPL", "MSFT", "TSLA"]  # Default stocks to monitor


def get_current_stock_prices(stocks):
    """
    Retrieve the current stock prices for the given stocks.

    Parameters:
        stocks (list of str): A list of stock symbols to monitor.

    Returns:
        dict: A dictionary mapping stock symbols to their current prices.
    """
    stock_prices = {}
    try:
        if len(stocks) == 1:
            ticker = yf.Ticker(stocks[0])
            data = ticker.history(period="1d", interval="1m")
            prices = data['Close'].values.tolist()
            stock_prices[stocks[0]] = prices[0]
        else:
            tickers = yf.Tickers(stocks)
            data = tickers.history(period="1d", interval="1m")
            prices = data['Close'].iloc[-1].tolist()
            for stock, price in zip(stocks, prices):
                stock_prices[stock] = price
        return stock_prices
    except yf.errors.YfinanceError as e:
        raise ValueError(str(e))


def print_stock_prices(stock_prices):
    """
    Print the current stock prices to the console.

    Parameters:
        stock_prices (dict): A dictionary mapping stock symbols to their current prices.
    """
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve current stock prices.")
    parser.add_argument("-s", "--stocks", nargs="+", help="List of stocks to monitor.")
    args = parser.parse_args()

    # Determine which stocks to monitor
    if args.stocks:
        query = args.stocks
    else:
        query = DEFAULT_STOCKS

    # Retrieve the current stock prices
    try:
        stock_prices = get_current_stock_prices(query)
        print_stock_prices(stock_prices)
    except ValueError as e:
        print(f"Invalid stock symbol: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
