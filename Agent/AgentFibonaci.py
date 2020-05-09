from . import TradeFunctions as ay
class AgentFibonaci():

	def __init__(self):
		self.data=[]
		self.avg=[]
		self.peaks=[]
		self.vally=[]
		self.trend="none"

	def getData(self,data,offset=0):
		self.data=data
		self.avg=ay.getMovingAvg(data,ran=20)
		self.peaks=ay.getPeaks(self.avg,secavg=10)
		self.vally=ay.getVally(self.avg,secavg=10)
		hh,lh,hl,ll = ay.getLowHigh(self.peaks,self.vally)
		#self.trend=ay.determineTrend(avg,offset=30)

		#prilagodimo da se bo prkazalo na plotu pravilno
		if offset>len(data):
			hh[0]=hh[0]+offset-len(data)
			lh[0]=lh[0]+offset-len(data)
			hl[0]=hl[0]+offset-len(data)
			ll[0]=ll[0]+offset-len(data)
		return hh,lh,hl,ll
