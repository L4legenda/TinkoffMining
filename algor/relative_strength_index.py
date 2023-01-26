import pandas as pd
import talib

def run(data):
    # Define the RSI period and threshold
    rsi_period = 14
    rsi_threshold = 70

    # Calculate the RSI
    data['RSI'] = talib.RSI(data['close'], timeperiod=rsi_period)

    # Initialize the position and profit variables
    position = 0
    profit = 0

    # Iterate through the data
    for i in range(len(data)):
        # Check if the RSI crosses above the threshold
        if data['RSI'][i] > rsi_threshold and position >= 0:
            # Sell
            position -= 1
            profit += data['close'][i]
        # Check if the RSI crosses below the threshold
        elif data['RSI'][i] < rsi_threshold and position <= 0:
            # Buy
            position += 1
            profit -= data['close'][i]

    profit = int(profit)
    
    # Print the final profit
    print("Profit RSI: ", profit)

    return {
        "profit": profit
    }