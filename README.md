# StockStack-CLI

Look up current stock prices from your terminal.

## INSTALLATION
1. Make sure to have [yfinance](https://pypi.org/project/yfinance/) installed
 
 `pip install yfinance`

2. Clone the repository

  `git clone https://github.com/carlobortolan/StockStack.git ~/stockstack`

3. Add <YOUR_ALIAS> as an alias to your _.bashrc_, _.zshrc_, etc.

  `echo 'alias <YOUR_ALIAS>="python3 ~/stockstack/caller.py"'>>~/.bashrc`

4. Update your _.bashrc_, _.zshrc_, etc.

  `source ~/.bashrc`

## HOW TO USE

```
 $ <YOUR_ALIAS> [-h] [-s STOCKS [STOCKS ...]]
```

```
Retrieve current stock prices.

options:
  -h, --help            show this help message and exit
  -s STOCKS [STOCKS ...], --stocks STOCKS [STOCKS ...]
                        List of stocks to monitor.
  -d DEFAULT_STOCKS [DEFAULT_STOCKS ...], --default_stocks DEFAULT_STOCKS [DEFAULT_STOCKS ...]
                        Set the default stocks to monitor.
```
