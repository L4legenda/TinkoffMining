import pandas as pd
import talib
import matplotlib.pyplot as plt

# Define the RSI period and threshold
rsi_period = 14
rsi_threshold = 70


def run(data):

    # Calculate the RSI
    data['RSI'] = talib.RSI(data['close'], timeperiod=rsi_period)

    # Initialize the position and profit variables
    position = 0
    profit = 0
    buy_times = []
    sell_times = []
    investment = 0

    # Iterate through the data
    for i in range(len(data)):
        # Check if the RSI crosses above the threshold
        if data['RSI'][i] > rsi_threshold and position >= 0:
            # Sell
            position -= 1
            profit += data['close'][i]
            sell_times.append(data.index[i])
        # Check if the RSI crosses below the threshold
        elif data['RSI'][i] < rsi_threshold and position <= 0:
            # Buy
            position += 1
            profit -= data['close'][i]
            investment += data['close'][i]
            buy_times.append(data.index[i])

    if investment != 0:
        percent_profit = round(profit / investment * 100, 2)
    else:
        percent_profit = 0
    profit = int(profit)

    # Print the final profit
    print("Profit RSI: ", profit)
    print("Percent Profit RSI: ", percent_profit)

    return {
        "profit": profit,
        "percent_profit": percent_profit,
        "buy_times": buy_times,
        "sell_times": sell_times,
    }


def view(data, buy_times, sell_times):
    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(10, 8))
    ax[0].plot(data.index, data['close'], label='Close Price')
    ax[0].legend()
    ax[1].plot(data.index, data['RSI'], label='RSI')
    ax[1].axhline(rsi_threshold, color='r', linestyle='--',
                  label='Overbought Threshold')
    ax[1].legend()

    # Plot the buy and sell signals
    ax[0].scatter(buy_times, data.loc[buy_times]['close'],
                  marker='^', color='g', label='Buy')
    ax[0].scatter(sell_times, data.loc[sell_times]['close'],
                  marker='v', color='r', label='Sell')
    ax[0].legend()

    plt.show()
