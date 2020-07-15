from . import TradeFunctions as ay
class AgentFibonaci():

	def __init__(self):
		self.data=[]
		self.avg=[]
		self.peaks=[]
		self.vally=[]
		self.trend="none"

	def getAction(self,data,offset=0):
		action = None
		self.data=data
		lastdata=data[-1]
		self.avg=ay.getMovingAvg(data,ran=10)
		self.peaks=ay.getPeaks(self.avg,secavg=10)
		self.vally=ay.getVally(self.avg,secavg=10)
		trend=ay.determineTrend(data,offset=150)
		if(trend==1):
			action= self.upTrendAnalyse()
		elif(trend==-1):
			action= self.downTrendAnalyse()
		'''
		hh,lh,hl,ll = ay.getLowHigh(self.peaks,self.vally)
		#prilagodimo da se bo prkazalo na plotu pravilno
		if offset>len(data):
			hh[0]=hh[0]+offset-len(data)
			lh[0]=lh[0]+offset-len(data)
			hl[0]=hl[0]+offset-len(data)
			ll[0]=ll[0]+offset-len(data)
		return hh,lh,hl,ll
		'''
		return action

	def downTrendAnalyse(self):
		return "sell"
	def upTrendAnalyse(self):
		return "buy"