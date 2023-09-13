import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock ticker and the month you want to track
stock_ticker = "SPY"  # SPY ticker symbol, tracks SPY 500.
start_date = "2000-09-01"
end_date = "2023-09-30"

# Fetch historical stock data
stock_data = yf.download(stock_ticker, start=start_date, end=end_date)

# Filter data to only include September records across multiple years
september_data = stock_data[stock_data.index.month == 9]

# Extract years and corresponding closing prices
years = september_data.index.year
closing_prices = september_data["Adj Close"]

# Create a line chart with years on the x-axis and closing prices on the y-axis
plt.figure(figsize=(10, 6))
plt.plot(years, closing_prices, marker='o', linestyle='-')
plt.title(f"{stock_ticker} Closing Prices in September Over the Years")
plt.xlabel("Year")
plt.ylabel("Closing Price")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.show()
