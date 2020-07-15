import pandas as pd
import AlphaVantage as av
from .Account import Account
import matplotlib.pyplot as plt 
from Agent import AgentFibonaci
import numpy as np
alphaVantageKey='3XCS4VQBPFZFGMX1'
#data1=av.getfxdata(alphaVantageKey,"EUR","USD","15min")
data2=pd.read_csv("Backtest/EURUSD.csv")
data2=data2['Close'].values[:]
data3=pd.read_csv("Backtest/EURGBP.csv",skipinitialspace=True)
data3=data3['value'].values[:]
data3=data3[0:4000]#start:stop:step
data4=pd.read_csv("Backtest/EURCHF.csv")
data4=data4[0:50000]
data4=data4.iloc[:,5].values[:]

#x=np.arange(0,2*np.pi,0.001)
#data3=np.sin(np.pi*x)

data=data4
a1=Account(1000,100)
a1.createMarket("EURGBP",data)
agentF=AgentFibonaci.AgentFibonaci()
odtipki=200
tick=0
while True:
	if not(tick%12) and tick>(odtipki-1):
		dataS=a1.getPrevMarketData("EURGBP",odtipki) #dobimo 150 odtipkov za nazaj
		action = agentF.getAction(dataS,offset=tick)
		a1.placeOrder("EURGBP",action,0.01,0.002,0.005)
	
	ended=a1.MarketTick()
	tick+=1
	if ended==True:
		#a1.closeAllOrders()
		break	

print(str(a1.getBalance()))
plt.plot(range(len(a1.getTotalMarketData("EURGBP"))),a1.getTotalMarketData("EURGBP"))
#plt.plot([item[0] for item in agentF.avg],[item[1] for item in agentF.avg],color='purple')
#plt.scatter([item[0] for item in agentF.peaks],[item[1] for item in agentF.peaks],color='orange')
#plt.scatter([item[0] for item in agentF.vally],[item[1] for item in agentF.vally],color='orange')
plt.scatter([item[0] for item in a1.marketOpenArray("EURGBP")],[item[1] for item in a1.marketOpenArray("EURGBP")],color='green')
plt.scatter([item[0] for item in a1.marketCloseArray("EURGBP")],[item[1] for item in a1.marketCloseArray("EURGBP")],color='red')

'''
plt.scatter(hh[0],hh[1],color='yellow')
plt.scatter(lh[0],lh[1],color='red')
plt.scatter(hl[0],hl[1],color='green')
plt.scatter(ll[0],ll[1],color='black')
'''



plt.show()

a1.deleteAllMarkets()

