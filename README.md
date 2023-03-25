# StockStack-CLI

Look up current stock prices from your terminal.

## INSTALLATION

1. Make sure to have [yfinance](https://pypi.org/project/yfinance/) installed

```
$ pip install yfinance
```

2. Clone the repository

```
$ git clone https://github.com/carlobortolan/StockStack.git ~/stockstack
```

3. Add <YOUR_ALIAS> as an alias to your _.bashrc_, _.zshrc_, etc.

```
$ echo 'alias <YOUR_ALIAS>="python3 ~/stockstack/caller.py"'>>~/.bashrc
```

> _**OPTIONAL**: If you want to have stockstack launch whenever you open a new terminal add:_
> ```
> $ echo '<YOUR_ALIAS>'>>~/.bashrc
> ```

4. Update your _.bashrc_, _.zshrc_, etc.

```
$ source ~/.bashrc
```

## HOW TO USE

Retrieve current stock prices.

```
$ <YOUR_ALIAS> [-h] [-s STOCKS [STOCKS ...]]
                 [-d DEFAULT_STOCKS [DEFAULT_STOCKS ...]]
                 [-u UPDATE_DEFAULT_STOCKS [UPDATE_DEFAULT_STOCKS ...]]
```

```
options:
  -h, --help            show this help message and exit
  -s STOCKS [STOCKS ...], --stocks STOCKS [STOCKS ...]
                        List of stocks to monitor.
  -d DEFAULT_STOCKS [DEFAULT_STOCKS ...], --default_stocks DEFAULT_STOCKS [DEFAULT_STOCKS ...]
                        Set the default stocks to monitor.
  -u UPDATE_DEFAULT_STOCKS [UPDATE_DEFAULT_STOCKS ...], --update_default_stocks UPDATE_DEFAULT_STOCKS [UPDATE_DEFAULT_STOCKS ...]
                        Update the default stocks.
```
