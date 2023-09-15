# INF601 - Advanced Programming in Python
# Gavin Stanley
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from pathlib import Path

def getClosing(ticker):
    # Get the closing price for the last 10 days
    stock = yf.Ticker(ticker)
    # get historical market data
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(price)

    return closingList

# Create a custom formatting function for the y-axis labels
def dollar_formatter(x, pos):
    return f"${x:.2f}"  # Format the number with a dollar sign and two decimal places

# Create our charts folder
try:
    Path("Charts").mkdir()
except FileExistsError:
    pass

stocks = ["MANU", "MSGS", "BATRA", "RCI", "CHDN"]

# Define a dictionary to map ticker symbols to stock names
stock_names = {
    "MANU": "Manchester United",
    "MSGS": "Madison Square Garden Sports",
    "BATRA": "Atlanta Braves",
    "RCI": "Toronto Blue Jays",
    "CHDN": "Churchill Downs",
}

for stock in stocks:
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing) + 1))

    # This plots the graph
    plt.plot(days, stockClosing)

    # Get our min and max for Y axis
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    # Set our X axis min and max
    plt.axis([1, 10, low_price - 1, high_price + 1])

    # Set the title of the graph using the stock name
    plt.title("Closing Price for " + stock_names.get(stock, "Unknown"))

    plt.xlabel("Days")

    # Set the y-axis labels with the custom dollar formatter
    plt.gca().yaxis.set_major_formatter(FuncFormatter(dollar_formatter))

    # Save plots
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    # Show the graph
    plt.show()