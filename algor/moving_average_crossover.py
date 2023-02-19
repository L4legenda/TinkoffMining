import pandas as pd
import talib
from matplotlib import pyplot as plt

# Define the short-term and long-term moving average periods
short_period = 10
long_period = 40


def run(data):

    # Calculate the moving averages
    data['short_ma'] = talib.SMA(data['close'], timeperiod=short_period)
    data['long_ma'] = talib.SMA(data['close'], timeperiod=long_period)

    # Initialize the position and profit variables
    position = 0
    profit = 0
    investment = 0

    buy_signals = []
    sell_signals = []

    # Iterate through the data
    for i in range(len(data)):
        # Check if the short-term moving average crosses above the long-term moving average
        if data['short_ma'][i] > data['long_ma'][i] and position <= 0:
            # Buy
            position += 1
            profit -= data['close'][i]
            investment += data['close'][i]
            buy_signals.append(i)

        # Check if the short-term moving average crosses below the long-term moving average
        elif data['short_ma'][i] < data['long_ma'][i] and position >= 0:
            # Sell
            position -= 1
            profit += data['close'][i]
            sell_signals.append(i)

    if investment != 0:
        percent_profit = round(profit / investment * 100, 2)
    else:
        percent_profit = 0

    profit = int(profit)

    # Print the final profit
    print("Profit SMA: ", profit)
    print("Percent Profit SMA: ", percent_profit)

    return {
        "profit": profit,
        "percent_profit": percent_profit,
        "buy_times": buy_signals,
        "sell_times": sell_signals,
    }


def view(data, buy_signals, sell_signals):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data['close'], label='Price')
    ax.plot(data['short_ma'], label=f'{short_period}-day SMA')
    ax.plot(data['long_ma'], label=f'{long_period}-day SMA')
    ax.scatter(buy_signals, data['close'][buy_signals],
               marker='^', color='g', label='Buy')
    ax.scatter(sell_signals, data['close'][sell_signals],
               marker='v', color='r', label='Sell')
    ax.legend()
    ax.set(title='Moving Average Crossover', xlabel='Date', ylabel='Price')

    # Show the chart
    plt.show()
