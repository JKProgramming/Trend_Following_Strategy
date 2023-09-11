# Import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Load GOOGL data from Yahoo Finance
data = pd.read_csv("GOOG.csv", index_col="Date", parse_dates=True)

# Calculate SMA-10 and EMA-50
data["SMA-10"] = data["Close"].rolling(10).mean()
data["EMA-50"] = data["Close"].ewm(span=50).mean()

# Plot the price and the moving averages
plt.figure(figsize=(12,8))
plt.plot(data["Close"], label="GOOGL")
plt.plot(data["SMA-10"], label="SMA-10")
plt.plot(data["EMA-50"], label="EMA-50")
plt.legend()
plt.title("Trend Following Strategy for GOOGL")
plt.show()

# Create a column for the signal
data["Signal"] = 0

# Generate buy and sell signals
data.loc[(data["SMA-10"] > data["EMA-50"]) & (data["Close"] > data["SMA-10"]), "Signal"] = 1 # buy
data.loc[(data["SMA-10"] < data["EMA-50"]) & (data["Close"] < data["SMA-10"]), "Signal"] = -1 # sell

# Print the first 10 rows of the signal column
print(data["Signal"].head(10))
