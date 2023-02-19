import pandas as pd
import talib

def run(data):

    # Define the Bollinger Band parameters
    bb_period = 20
    bb_deviation = 2

    # Calculate the Bollinger Bands
    data['upper_band'], data['middle_band'], data['lower_band'] = talib.BBANDS(data['close'], timeperiod=bb_period, nbdevup=bb_deviation, nbdevdn=bb_deviation)

    # Initialize the position and profit variables
    position = 0
    profit = 0
    investment = 0

    # Iterate through the data
    for i in range(len(data)):
        # Check if the close price crosses above the upper Bollinger Band
        if data['close'][i] > data['upper_band'][i] and position >= 0:
            # Sell
            position -= 1
            profit += data['close'][i]
        # Check if the close price crosses below the lower Bollinger Band
        elif data['close'][i] < data['lower_band'][i] and position <= 0:
            # Buy
            position += 1
            investment += data['close'][i]
            profit -= data['close'][i]

    if investment != 0:
        percent_profit = round(profit / investment * 100, 2)
    else:
        percent_profit = 0

    profit = int(profit)
    # Print the final profit
    print("Profit BB: ", profit)
    print("Percent Profit BB: ", percent_profit)

    return {
        "profit": profit,
        "percent_profit": percent_profit,
    }