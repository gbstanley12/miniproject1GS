# INF601 - Advanced Programming in Python
# Gavin Stanley
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

#Man United = MANU
#Madison Square Garden Sports = MSGS
#Braves = BATRA
#Blue Jays = RCI
#Churchhill Downs = CHDN
def getClosing(ticker):
    #Get the closing price for the last 10 days
    stock = yf.Ticker(ticker)
    # get historical market data
    hist = stock.history(period="10d")

    closingList = []

    for price in hist['Close']:
        closingList.append(price)

    return closingList

#Create our charts folder
try:
    Path("Charts").mkdir()
except FileExistsError:
    pass

stocks = ["MSFT", "GME", "AAPL", "SONY", "META"]

for stock in stocks:
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing)+1))

    #This plots the graph
    plt.plot(days, stockClosing)

    #Get our min and max for Y axis
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    #Set our X axis min and max
    plt.axis([1, 10, low_price-2, high_price+2])

    # Set our lables for the graph
    plt.title("Closing Price for " + stock)
    plt.xlabel("Days")
    plt.ylabel("Closing Price")

    #Saves plots
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)

    #Shows the graph
    plt.show()