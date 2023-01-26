import pandas as pd
import talib

def run(data):

    # Define the short-term and long-term moving average periods
    short_period = 30
    long_period = 100

    # Calculate the moving averages
    data['short_ma'] = talib.SMA(data['close'], timeperiod=short_period)
    data['long_ma'] = talib.SMA(data['close'], timeperiod=long_period)

    # Initialize the position and profit variables
    position = 0
    profit = 0

    # Iterate through the data
    for i in range(len(data)):
        # Check if the short-term moving average crosses above the long-term moving average
        if data['short_ma'][i] > data['long_ma'][i] and position <= 0:
            # Buy
            position += 1
            profit -= data['close'][i]
        # Check if the short-term moving average crosses below the long-term moving average
        elif data['short_ma'][i] < data['long_ma'][i] and position >= 0:
            # Sell
            position -= 1
            profit += data['close'][i]

    profit = int(profit)
    
    # Print the final profit
    print("Profit SMA: ", profit)

    return {
        "profit": profit
    }