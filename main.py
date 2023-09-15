# INF601 - Advanced Programming in Python
# Gavin Stanley
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path

# Function to get the long name of a stock based on its ticker symbol
def getStockName(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return info.get("longName", "Unknown")

# Function to get the closing prices of a stock for the last 10 days
def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")
    closingList = []
    for price in hist['Close']:
        closingList.append(price)
    return closingList

# Function for custom formatting of y-axis labels with a dollar sign
def dollar_formatter(x, pos):
    return f"${x:.2f}"

try:
    # Create a "Charts" directory if it doesn't exist
    Path("Charts").mkdir()
except FileExistsError:
    pass

# List of stock ticker symbols
stocks = ["MANU", "MSGS", "BATRA", "RCI", "CHDN"]

# Loop through each stock
for stock in stocks:
    # Get the long name of the stock
    stockName = getStockName(stock)
    # Get the closing prices
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing) + 1))

    # Plot the graph
    plt.plot(days, stockClosing)

    # Get the min and max prices for Y-axis
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # Set the X and Y axis limits
    plt.axis([1, 10, low_price - 1, high_price + 1])

    # Set the title of the graph using the stock's long name
    plt.title(f"Closing Price for {stockName}")
    plt.xlabel("Days")

    # Format Y-axis labels with a dollar sign
    plt.gca().yaxis.set_major_formatter(FuncFormatter(dollar_formatter))

    # Save the plot as an image
    savefile = f"charts/{stock}.png"
    plt.savefig(savefile)

    # Show the graph
    plt.show()