class Stock:
    def __init__(self, symbol = "$", name = " ", previousClosingPrice = 3000, currentPrice = 2000):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = 3000
        self.__currentPrice = 2000
    def getStockName(self):
        return self.__name
    def getSymbol(self):
        return self.__symbol
    def getpreviousClosingPrice(self):
        return self.__previousClosingPrice
    def getcurrentPrice(self):
        return self.__currentPrice
    def setpreviousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice
    def setcurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice
    def getChangePercent(self):
        return (str((self.__currentPrice-self.__previousClosingPrice)/self.__previousClosingPrice * 100) + "%")
j = Stock().setpreviousClosingPrice(5000)
print(Stock().getpreviousClosingPrice())
stock1 = Stock("INTC", "David", 20.5, 20.35)
stock2 = Stock("ITc", "Dan", 4000, 5000)
print(stock1.getChangePercent())