import yfinance as yf
import argparse
from typing import List, Dict, Any
from pathlib import Path

DEFAULT_STOCKS_FILE = "default_stocks.txt"  # Default stocks to monitor


def read_default_stocks() -> List[str]:
    """
    Read the default stocks from the DEFAULT_STOCKS_FILE file.

    Returns:
        list: A list of default stock symbols.
    """
    default_stocks_file = Path(__file__).resolve().parent / DEFAULT_STOCKS_FILE
    try:
        with open(default_stocks_file, "r") as f:
            default_stocks = f.read().splitlines()
        return default_stocks
    except IOError:
        print(f"Could not read {DEFAULT_STOCKS_FILE}")
        return []


def write_default_stocks(default_stocks: List[str]) -> None:
    """
    Write the default stocks to the DEFAULT_STOCKS_FILE file.

    Parameters:
        default_stocks (list of str): A list of stock symbols to monitor.
    """
    default_stocks_file = Path(__file__).resolve().parent / DEFAULT_STOCKS_FILE
    try:
        with open(default_stocks_file, "w") as f:
            f.write("\n".join(default_stocks))
            print(f"Default stocks updated: {', '.join(default_stocks)}")
    except IOError:
        print(f"Could not write {DEFAULT_STOCKS_FILE}")


def update_default_stocks(new_stocks: List[str]) -> List[str]:
    """
    Update the default stocks with new_stocks.

    Parameters:
        new_stocks (list of str): A list of new stock symbols to add to the default stocks.

    Returns:
        list: The updated list of default stocks.
    """
    default_stocks = read_default_stocks()
    for s in new_stocks:
        if s not in default_stocks:
            default_stocks.append(s)
    write_default_stocks(default_stocks)
    return default_stocks


DEFAULT_STOCKS = read_default_stocks() or ["AAPL", "MSFT", "TSLA"]


def get_current_stock_prices(stocks: List[str] = None, details: str = None) -> Dict[str, Any]:
    """
    Retrieve and display the current stock prices for the given stocks.

    Parameters:
        stocks (list of str): A list of stock symbols to monitor.
        details (str): Additional details to display about the specified stock.

    Returns:
        dict: A dictionary mapping stock symbols to their current prices.
    """
    if stocks is None:
        stocks = DEFAULT_STOCKS
    try:
        if len(stocks) == 1:
            ticker = yf.Ticker(stocks[0])
        else:
            ticker = yf.Tickers(stocks)

        data = ticker.history(period="1d", interval="1m")
        prices = data['Close'].values.tolist()
        stock_prices = {}

        for stock, price in zip(stocks, prices):
            stock_prices[stock] = price
            if details:
                ticker = yf.Ticker(stock)
                mh = ticker.major_holders
                info = ticker.fast_info.toJSON()
                print(f"{stock}: ${price:}, {info}")
                print(f"{mh}")
            else:
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
    parser.add_argument("-u", "--update_default_stocks", nargs="+", help="Update the default stocks.")
    parser.add_argument('--details', nargs='?', const=True, help='Display additional details about a stock.')
    args = parser.parse_args()

    # Update the default stocks if requested
    if args.update_default_stocks:
        DEFAULT_STOCKS = update_default_stocks(args.update_default_stocks)

    # Set the default stocks if provided
    if args.default_stocks:
        DEFAULT_STOCKS = args.default_stocks
        write_default_stocks(DEFAULT_STOCKS)

    # Determine which stocks to monitor
    if args.stocks:
        query = args.stocks
    else:
        query = DEFAULT_STOCKS

    # Retrieve and display the current stock prices
    if args.details:
        get_current_stock_prices(query, args.details)
    else:
        get_current_stock_prices(query)
