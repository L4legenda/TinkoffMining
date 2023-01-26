import pandas as pd
import matplotlib.pyplot as plt
from talib import abstract

# Load data and calculate Fibonacci retracements
df = pd.read_csv('crypto_data.csv')
df['FIB_38.2%'], df['FIB_61.8%'] = abstract.FIBONACCI(df, 38.2), abstract.FIBONACCI(df, 61.8)

# Visualize data and Fibonacci retracements
plt.plot(df['Close'])
plt.plot(df['FIB_38.2%'])
plt.plot(df['FIB_61.8%'])
plt.show()

# Use Fibonacci retracements to identify entry and exit points
for i in range(1, len(df)):
    # If price crosses above 38.2% retracement, buy
    if df['Close'][i] > df['FIB_38.2%'][i] and df['Close'][i-1] <= df['FIB_38.2%'][i-1]:
        print('BUY at', df['Close'][i])
    # If price crosses below 61.8% retracement, sell
    elif df['Close'][i] < df['FIB_61.8%'][i] and df['Close'][i-1] >= df['FIB_61.8%'][i-1]:
        print('SELL at', df['Close'][i])