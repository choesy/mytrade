from .Market import Market

class Account:
	def __init__(self,initialMoney,leverage):
		self.leverage=leverage
		self.MarketList=list()
		self.initialMoney=initialMoney
		self.balance=initialMoney
		self.maxLotSize=leverage*initialMoney/100000

	def createMarket(self,marketName,marketData):
		market=Market(marketName,marketData)	
		self.MarketList.append(market)

	def getBalance(self):
		return self.balance

	def getCurrentMarketData(self,marketName):	
		for market in self.MarketList:
			if marketName==market.marketName:
				return market.getCurrentMarketData()
		return 0
		
	def getTotalMarketData(self,marketName):		
		for market in self.MarketList:
			if marketName==market.marketName:
				return market.getTotalMarketData()

	def getPrevMarketData(self,marketName,num):		
		for market in self.MarketList:
			if marketName==market.marketName:
				return market.getPrevMarketData(num)

	def placeOrder(self,marketName,action,lot,stopLoss,takeProfit):
		#stopLoss in takeprofit so Procentih 0..1
		stopLoss=stopLoss*lot*100000 #kolicina denarja ki si jo pripravljen izgubit v EUR, torej procennti od tvojega ballance (upoštevati se mora lot) 
		takeProfit=takeProfit*lot*100000
		print(takeProfit)
		if lot>self.maxLotSize:
			print("insufficient money")
		else:
			for market in self.MarketList:
				if marketName==market.marketName:
					if(action==None):
						return
					orderID=market.orderCreate(action,lot,stopLoss,takeProfit)
					return marketName,orderID

	def closeAllOrders(self,marketName="all"):
		if marketName=="all":
			for market in self.MarketList:
				self.updateBalance(market.closeAllOrders())
		else:
			for market in self.MarketList:
				if marketName==market.marketName:
					self.updateBalance(market.closeAllOrders())

	def closeOrder(self,MarketNameAndOrderID):
		for market in self.MarketList:
				if MarketNameAndOrderID[0]==market.marketName:
					self.updateBalance(market.closeOrder(MarketNameAndOrderID[1]))

	def updateBalance(self,moneyDiff):
		self.balance=self.balance+moneyDiff
		self.maxLotSize=self.balance*self.leverage/100000

	def marketOpenArray(self,marketName):
		for market in self.MarketList:
			if marketName==market.marketName:
				return market.openArray

	def marketCloseArray(self,marketName):
		for market in self.MarketList:
			if marketName==market.marketName:
				return market.closeArray

	def MarketTick(self):
		marketLen=len(self.MarketList)
		endedCount=0
		for market in self.MarketList:
			if market.simulationEnded == False:
				totalDiff=market.marketTickReturnResult()	
				self.updateBalance(totalDiff)
			else:
				endedCount+=1	
		return endedCount==marketLen
		if (self.balance<=0):
			return True

	def deleteAllMarkets(self):
		for market in self.MarketList:
			self.MarketList.remove(market)

	
		


		
