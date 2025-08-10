# futures_indicators.py
This project demonstrates my understanding of trade execution strategies (primarily for equities and futures), focusing on the Volume Weighted Average Price (VWAP) and Average True Range (ATR). These indicators are essential to manage execution risk and market volatility in trading, and are also used in my extended trading strategy which I have coded. While the complete strategy is not shared publicly, I can discuss in more detail during interviews or screen shares.

VWAP: The VWAP is a benchmark used by portfolio managers and is an important execution strategy in low-touch trading. During my time at AXA Investment Managers, I spent time with the Head of Equity Execution Trading, where we discussed how VWAP is used to route trade orders via algowheels, allowing for efficient and low-impact order execution. It helps ensure trades are executed at an average price, minimising market impact.

ATR: The idea of implementing the ATR was due to my understanding of volatilty regimes, where periods of high volatility in asset prices are often followed by other periods of high volatility, and vice versa. An example would be when I spent time shadowing at the desk of AXA IM, market volatility across most asset classes was low. The FI desk especially did not have much volatitlity. This means large swings in price movement was unlikely, and this was demonstrated by low ATR values respective to other months, such as April.

ATR is useful in determining risk management levels, for example my trading strategy's risk management is largely determined by market volatitly. It is intutitive, that high volatility means more slippage and worse price fills. This is partly due to sellside widening spreads, where they want to protect their inventory, fear of asymmetric information, or want to capitalise of buyside urgency. Also maximum adverse excursion is likely to be larger when volatility is high, which helps determine risk limits and position sizing.

Example Output (this is directly from my terminal):
  date and time      open      high       low     close  volume      vwap  atr14
588916 2025-08-03 23:00:00  22850.00  22897.25  22846.25  22866.50    1708  22870.00  10.39
588917 2025-08-03 23:03:00  22866.00  22879.00  22840.50  22857.75    1759  22864.46  12.55
588918 2025-08-03 23:06:00  22856.75  22859.50  22836.75  22839.50     804  22860.84  13.80
588919 2025-08-03 23:09:00  22839.25  22849.00  22821.75  22833.00     926  22856.17  14.79
588920 2025-08-03 23:12:00  22832.50  22838.25  22826.50  22832.25     375  22854.56  14.73
...                    ...       ...       ...       ...       ...     ...       ...    ...
589167 2025-08-04 11:33:00  23066.50  23072.50  23066.50  23071.50     178  22969.58   6.95
589168 2025-08-04 11:36:00  23072.50  23073.50  23059.50  23059.50     404  22970.06   7.73
589169 2025-08-04 11:39:00  23059.50  23074.50  23059.50  23070.75     775  22970.99   8.20
589170 2025-08-04 11:42:00  23070.50  23078.00  23067.50  23070.00     339  22971.41   8.30
589171 2025-08-04 11:45:00  23069.50  23070.00  23065.00  23065.00     102  22971.53   8.34

[256 rows x 8 columns]
