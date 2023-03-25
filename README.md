# StockStack-CLI

Look up current stock prices from your terminal.

This is a Python script for monitoring the current stock prices using the Yahoo Finance API to retrieve the latest
stock prices and display them in the terminal.

## INSTALLATION

1. Make sure to have [yfinance](https://pypi.org/project/yfinance/) installed

```
$ pip install yfinance
```

2. Clone this repository to your local machine

```
$ git clone https://github.com/carlobortolan/StockStack.git ~/stockstack
```

3. Add <YOUR_ALIAS> as an alias to your _.bashrc_, _.zshrc_, etc.

```
$ echo 'alias <YOUR_ALIAS>="python3 ~/stockstack/caller.py"'>>~/.bashrc
```

> _**OPTIONAL**: If you want to have StockStack launch whenever you open a new terminal add:_
> ```
> $ echo '<YOUR_ALIAS>'>>~/.bashrc
> ```

4. Update your _.bashrc_, _.zshrc_, etc.

```
$ source ~/.bashrc
```

## USAGE

Retrieve current stock prices.

```
$ <YOUR_ALIAS>   [] [-h] [-s STOCKS [STOCKS ...]]
                 [-d DEFAULT_STOCKS [DEFAULT_STOCKS ...]]
                 [-u UPDATE_DEFAULT_STOCKS [UPDATE_DEFAULT_STOCKS ...]]
                 [--details [DETAILS]]
```

```
options:
options:
  -h, --help            show this help message and exit
  -s STOCKS [STOCKS ...], --stocks STOCKS [STOCKS ...]
                        List of stocks to monitor.
  -d DEFAULT_STOCKS [DEFAULT_STOCKS ...], --default_stocks DEFAULT_STOCKS [DEFAULT_STOCKS ...]
                        Set the default stocks to monitor.
  -u UPDATE_DEFAULT_STOCKS [UPDATE_DEFAULT_STOCKS ...], --update_default_stocks UPDATE_DEFAULT_STOCKS [UPDATE_DEFAULT_STOCKS ...]
                        Update the default stocks.
  --details [DETAILS]   Display additional details about a stock.
```

## EXAMPLES

> _**NOTE**: Replace with your alias if necessary._

To retrieve the current stock prices for a list of stocks, run the script with the following command:

```
python stock_price_monitor.py -s AAPL MSFT TSLA
```

This will display the current prices for Apple, Microsoft and Tesla stocks.

To set the default stocks to monitor, use the `-d` or `--default_stocks` option:

```
python stock_price_monitor.py -d AAPL MSFT
```

This will set the default stocks to Apple and Microsoft.

To update the default stocks, use the `-u` or `--update_default_stocks` option:

```
python stock_price_monitor.py -u AAPL GOOG
```

This will add Apple and Google stocks to the default list (if not already added).

To view the current price of your default list run the script without any options:

```
python stock_price_monitor.py
```

## CONTRIBUTING

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull
request.

## LICENSE

This project is licensed under the GPL-3.0 license. See the [LICENSE](LICENSE) file for details.