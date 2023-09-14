# INF601 - Advanced Programming in Python
# Gavin Stanley
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

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


#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.