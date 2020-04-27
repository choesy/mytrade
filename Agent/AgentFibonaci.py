from . import TradeFunctions as ay
class AgentFibonaci():

	def __init__(self):
		self.data=[]
		self.avg=[]
		self.peaks=[]
		self.vally=[]
		self.trend="none"

	def updateAgentData(self,data):
		self.data=data
		avg=ay.getMovingAvg(data,ran=50)
		self.avg=avg
		self.peaks=ay.getPeaks(data,avg)
		self.vally=ay.getVally(data,avg)
		self.trend=ay.determineTrend(avg,offset=50)
