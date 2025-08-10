import pandas as pd

# I have imported 5 years of CGQ Quantower data into CSV format, uploaded to VScode
df = pd.read_csv("@NQ - 3 min - ETH.csv",
                 # I call column 1 date and time instead of datetime to avoid confusion with pd.to_datetime function
                 names=["date and time", "open", "high", "low", "close", "volume"])

# Format for turning CSV data into readable date and time
df["date and time"] = pd.to_datetime(
    df["date and time"], format="%Y%m%d %H%M%S")

# HLC3 for VWAP
# Standard calculation most trading platforms (in my experience) use
df["hlc3"] = (df["high"] + df["low"] + df["close"]) / 3

# ATR(14) for 3-minute NQ
df["previous_close"] = df["close"].shift(1)
df["true range"] = df[["high", "previous_close"]].max(
    axis=1) - df[["low", "previous_close"]].min(axis=1)
df["atr14"] = df["true range"].rolling(window=14).mean()

# Session start starting at 23:00
df["session_date"] = df["date and time"].dt.date
df.loc[df["date and time"].dt.hour < 23,
       "session_date"] = df["session_date"] - pd.Timedelta(days=1)

# Get last session only
last_session = df["session_date"].max()
df_last = df[df["session_date"] == last_session].copy()

# VWAP calculation for last session
df_last["cum_vol_price"] = (df_last["hlc3"] * df_last["volume"]).cumsum()
df_last["cum_vol"] = df_last["volume"].cumsum()
df_last["vwap"] = df_last["cum_vol_price"] / df_last["cum_vol"]

# Round VWAP & ATR to 2 decimal places which most trading platforms do
df_last["vwap"] = df_last["vwap"].round(2)
df_last["atr14"] = df_last["atr14"].round(2)

# Final Output
df_last = df_last[["date and time", "open", "high",
                   "low", "close", "volume", "vwap", "atr14"]]
print(df_last)
