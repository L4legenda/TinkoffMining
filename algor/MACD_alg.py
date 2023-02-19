import pandas as pd
import talib


def run(data):

    # Define the MACD parameters
    macd_fast_period = 12
    macd_slow_period = 26
    macd_signal_period = 9

    # Calculate the MACD
    data['macd'], data['macd_signal'], data['macd_hist'] = talib.MACD(
        data['close'], fastperiod=macd_fast_period, slowperiod=macd_slow_period, signalperiod=macd_signal_period)

    # Initialize the position and profit variables
    position = 0
    profit = 0
    investment = 0

    # Iterate through the data
    for i in range(len(data)):
        # Check if the MACD crosses above the signal line
        if data['macd'][i] > data['macd_signal'][i] and position <= 0:
            # Buy
            position += 1
            investment += data['close'][i]
            profit -= data['close'][i]
        # Check if the MACD crosses below the signal line
        elif data['macd'][i] < data['macd_signal'][i] and position >= 0:
            # Sell
            position -= 1
            profit += data['close'][i]

    if investment != 0:
        percent_profit = round(profit / investment * 100, 2)
    else:
        percent_profit = 0

    profit = int(profit)

    # Print the final profit
    print("Profit MACD: ", profit)
    print("Percent Profit MACD: ", percent_profit)

    return {
        "profit": profit,
        "percent_profit": percent_profit,
    }
