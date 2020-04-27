import pandas as pd

def getPeaks(data,avg,ran):
	avgoffset=ran
	prevval=data[avgoffset-1]
	newval=0
	rising=False
	out=pd.DataFrame(columns = ['Date', 'Val'])
	for i in range(avgoffset,len(avg)+avgoffset):
		newval=data[i]
		if (prevval>newval and rising==True):
			newval=data[i-1]
			rising=False
			if(newval>avg[avg.Date==data.index.values[i-1]]['Val'].item()):
				out=out.append({'Date':data.index.values[i-1],'Val':data[i-1]}, ignore_index=True)
		if prevval<newval:
			rising=True
		prevval=newval
	return out

def getVally(data,avg,ran):
	avgoffset=ran
	prevval=data[avgoffset-1]
	newval=0
	rising=False
	out=pd.DataFrame(columns = ['Date', 'Val'])
	for i in range(avgoffset,len(avg)+avgoffset):
		newval=data[i]
		if (prevval<newval and rising==True):
			newval=data[i-1]
			rising=False
			if(newval<avg[avg.Date==data.index.values[i-1]]['Val'].item()):
				out=out.append({'Date':data.index.values[i-1],'Val':data[i-1]}, ignore_index=True)
		if prevval>newval:
			rising=True
		prevval=newval
	return out

def getMovingAvg(data,ran=3):
	out=pd.DataFrame(columns = ['Date', 'Val'])
	for i in range(ran,len(data)-ran):
		avgval=data.iloc[i-ran:i+ran].sum()/(2*ran)
		out=out.append({'Date':data.index.values[i],'Val':avgval}, ignore_index=True)
	return out

def determineTrend(avg,offset=1):
	if avg[-1]>avg[-(1+offset)]:
		return "up"
	elif avg[-1]<avg[-(1+offset)]:
		return "down"
	else:
		return "none"

