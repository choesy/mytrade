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
		self.avg=ay.getMovingAvg(data,ran=20)
		self.peaks=ay.getPeaks(self.avg,secavg=5)
		self.vally=ay.getVally(self.avg,secavg=5)
		hh,lh,hl,ll = ay.getLowHigh(self.peaks,self.vally)
		trend=ay.determineTrend(data,offset=30)
		if (hh[0]<ll[0] and trend>0 ):
			action=self.upTrendAnalyse()
		elif(ll[0]<hh[0] and trend<0):
			action=self.downTrendAnalyse()
		deviation=ay.getDeviation(self.avg,data)
		'''
		#prilagodimo da se bo prkazalo na plotu pravilno
		if offset>len(data):
			hh[0]=hh[0]+offset-len(data)
			lh[0]=lh[0]+offset-len(data)
			hl[0]=hl[0]+offset-len(data)
			ll[0]=ll[0]+offset-len(data)
		return hh,lh,hl,ll
		'''
		return action,deviation

	def downTrendAnalyse(self):
		return "sell"
	def upTrendAnalyse(self):
		return "buy"