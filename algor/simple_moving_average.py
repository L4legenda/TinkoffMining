import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def run(df, graphic=False):
    SMA30 = pd.DataFrame()
    SMA30['close'] = df['close'].rolling(window=30).mean()

    SMA100 = pd.DataFrame()
    SMA100['close'] = df['close'].rolling(window=100).mean()

    df_prices = pd.DataFrame()
    df_prices['date'] = df['date']
    df_prices['close'] = df['close']
    df_prices['close SMA30'] = SMA30['close']
    df_prices['close SMA100'] = SMA100['close']

    dual_sma_result = dual_sma(df_prices)
    df_prices["buy signal price"] = dual_sma_result[0]
    df_prices["sell signal price"] = dual_sma_result[1]

    if graphic:
        visualise_data(df_prices)


def visualise_data(df_prices):
    plt.figure(figsize=(13,15))

    plt.plot(df_prices['close'], label="Close price", alpha=0.6)
    plt.plot(df_prices['close SMA30'], label="SMA30", linewidth=3)
    plt.plot(df_prices['close SMA100'], label="SMA100", linewidth=3)

    plt.scatter(df_prices.index, df_prices['buy signal price'], label="Buy signal", color='green', marker='^', linewidth=5)
    plt.scatter(df_prices.index, df_prices['sell signal price'], label="Sell signal", color='red', marker='v', linewidth=5)

    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend(loc="upper left")
    plt.show()


def dual_sma(df):
    buy_signal_price = []
    sell_signal_price = []
    flag = 0

    for i in range(len(df)):
        if df['close SMA30'][i] > df["close SMA100"][i]:
            if flag != 1:
                buy_signal_price.append(df['close'][i])
                sell_signal_price.append(np.nan)
                flag = 1
            else:
                buy_signal_price.append(np.nan)
                sell_signal_price.append(np.nan)
        elif df['close SMA30'][i] < df["close SMA100"][i]:
            if flag != -1:
                buy_signal_price.append(np.nan)
                sell_signal_price.append(df['close'][i])
                flag = -1
            else:
                buy_signal_price.append(np.nan)
                sell_signal_price.append(np.nan)
        else:
            buy_signal_price.append(np.nan)
            sell_signal_price.append(np.nan)
    return (buy_signal_price, sell_signal_price)