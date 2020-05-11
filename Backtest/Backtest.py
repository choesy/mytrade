import pandas as pd
import AlphaVantage as av
from .Account import Account
import matplotlib.pyplot as plt 
from Agent import AgentFibonaci
import numpy as np
alphaVantageKey='3XCS4VQBPFZFGMX1'
data1=av.getfxdata(alphaVantageKey,"EUR","USD","15min")
#data2=pd.read_csv("Backtest/EURUSD.csv")
#data2=data2['Close'].values[:]
data3=pd.read_csv("Backtest/EURGBP.csv",skipinitialspace=True)
data3=data3['value'].values[:]
data3=data3[2000:4000]#start:stop:step
#x=np.arange(0,2*np.pi,0.001)
#data3=np.sin(6*np.pi*x)
a1=Account(10000,100)
a1.createMarket("EURGBP",data1)
agentF=AgentFibonaci.AgentFibonaci()
backdatalen=345
print(len(data1))

tick=0
while True:
	currentVal1=a1.getCurrentMarketData("EURGBP")
	if (tick==10):
		#data=a1.getPrevMarketData("EURGBP",150)
		data=data1
		hh,lh,hl,ll = agentF.getData(data,offset=len(data1))
	if (tick==270):
		order1=a1.placeOrder("EURGBP","buy",0.1,0,0)

	if (tick==500):
		a1.closeOrder(order1)
	
	ended=a1.MarketTick()
	tick+=1
	if ended==True:
		a1.closeAllOrders()
		break	

print(str(a1.getBalance()))
plt.plot(range(len(a1.getTotalMarketData("EURGBP"))),a1.getTotalMarketData("EURGBP"))
plt.plot([item[0] for item in agentF.avg],[item[1] for item in agentF.avg],color='purple')
plt.scatter([item[0] for item in agentF.peaks],[item[1] for item in agentF.peaks],color='orange')
plt.scatter([item[0] for item in agentF.vally],[item[1] for item in agentF.vally],color='orange')
plt.scatter([item[0] for item in a1.marketOpenArray("EURGBP")],[item[1] for item in a1.marketOpenArray("EURGBP")],color='green')
plt.scatter([item[0] for item in a1.marketCloseArray("EURGBP")],[item[1] for item in a1.marketCloseArray("EURGBP")],color='red')


plt.scatter(hh[0],hh[1],color='yellow')
plt.scatter(lh[0],lh[1],color='red')
plt.scatter(hl[0],hl[1],color='green')
plt.scatter(ll[0],ll[1],color='black')




plt.show()

a1.deleteAllMarkets()

