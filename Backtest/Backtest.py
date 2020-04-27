import pandas as pd
import AlphaVantage as av
from .Account import Account
import matplotlib.pyplot as plt 
alphaVantageKey='3XCS4VQBPFZFGMX1'
data=av.getfxdata(alphaVantageKey,"EUR","USD","15min")
data2=pd.read_csv("Backtest/EURUSD.csv")
data2=data2['Close'].values[:]
data3=pd.read_csv("Backtest/EURGBP.csv",skipinitialspace=True)
data3=data3['value'].values[:]
data3=data3[0:5554:4]#start:stop:step
a1=Account(10000,100)
a1.createMarket("EURUSD",data2)
a1.createMarket("EURGBP",data3)
tick=0
while True:
	currentVal1=a1.getCurrentMarketData("EURGBP")
	if (tick==30):
		order1=a1.placeOrder("EURGBP","buy",0.1,0.01,0.01)
	
	if (tick==300):
		order2=a1.placeOrder("EURGBP","buy",0.1,0,0)

	if (tick==500):
		order3=a1.placeOrder("EURGBP","buy",0.1,0,0)

	if (tick==800):
		a1.closeOrder(order3)
	
	ended=a1.MarketTick()
	tick+=1
	if ended==True:
		a1.closeAllOrders()
		break	

print(str(a1.getBalance()))
print(a1.marketOpenArray("EURGBP"))
plt.plot(range(len(data3)),data3)
plt.scatter([item[0] for item in a1.marketOpenArray("EURGBP")],[item[1] for item in a1.marketOpenArray("EURGBP")],color='green')
plt.scatter([item[0] for item in a1.marketCloseArray("EURGBP")],[item[1] for item in a1.marketCloseArray("EURGBP")],color='red')
a1.deleteAllMarkets()
plt.show()


