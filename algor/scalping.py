import pandas as pd

def run(data):

    # Define the scalping parameters
    profit_threshold = 0.1 # 10% profit
    stop_loss_threshold = -0.05 # 5% loss

    # Initialize the position and profit variables
    position = 0
    profit = 0

    # Iterate through the data
    for i in range(1,len(data)):
        if position == 0:
            # Check if the current close price is greater than the previous close price
            if data['close'][i] > data['close'][i-1]:
                # Buy
                position += 1
                entry_price = data['close'][i]
        else:
            # Calculate the current profit
            current_profit = (data['close'][i] - entry_price) / entry_price
            # Check if the current profit is greater than the profit threshold
            if current_profit > profit_threshold:
                # Sell
                position -= 1
                profit += current_profit
            # Check if the current profit is less than the stop loss threshold
            elif current_profit < stop_loss_threshold:
                # Sell
                position -= 1
                profit += current_profit

    profit = int(profit)
    
    # Print the final profit
    print("Profit scalping: ", profit)

    return {
        "profit": profit
    }