
class Orders:
	def __init__(self,startingValue,action,lot,stopLoss,takeProfit,orderID):
		self.startingValue=startingValue
		self.action=action
		self.orderID=orderID
		self.stopLossPip=stopLoss
		self.takeProfitPip=takeProfit
		self.lot=lot
		if action=="buy":
			self.stopLoss=startingValue-stopLoss/100000
			self.takeProfit=startingValue+takeProfit/100000
		elif action=="sell":
			self.stopLoss=startingValue+stopLoss/100000 #convertiranje v pipe
			self.takeProfit=startingValue-takeProfit/100000
		else:
			raise EnvironmentError #ni ne buy ne sell
		
	def checkIfReadyToClose(self,currentValue):
		moneyMade=None
		if self.action=="buy":
			if (currentValue>=self.takeProfit) and (self.takeProfitPip>0):
				moneyMade=self.closeOrder(currentValue)
			elif (currentValue<=self.stopLoss) and (self.stopLossPip>0):
				moneyMade=self.closeOrder(currentValue)

		elif self.action=="sell":
			if (currentValue<=self.takeProfit) and (self.takeProfitPip>0):
				moneyMade=self.closeOrder(currentValue)
			elif (currentValue>=self.stopLoss) and (self.stopLossPip>0):
				moneyMade=self.closeOrder(currentValue)
		else:
			raise EnvironmentError #mora bit buy ali sell
		return moneyMade


	def closeOrder(self,currentValue):
		if self.action=="buy":
			diff=currentValue-self.startingValue #dobimo številko pipov
		elif self.action=="sell":
			diff=self.startingValue-currentValue
		return diff*100000*self.lot #moramo pomnožit pipe z 100000 in z self.lot da dobimo dejansko denarno razliko

