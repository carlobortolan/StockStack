import yfinance as yf

# Define a function to retrieve and display the current stock prices
def get_current_stock_prices(stocks):
    # Retrieve the current stock prices using the yfinance library
    tickers = yf.Tickers(stocks)
    data = tickers.history(period="1d")
    prices = data['Close'].values.tolist()
    # Display the current stock prices in the terminal
    for stock, price in zip(stocks, prices):
        print(f"{stock}: {price}")

# Define a list of stocks to monitor
stocks = ["AAPL", "MSFT", "GOOG"]

# Call the function to retrieve and display the current stock prices
get_current_stock_prices(stocks)
