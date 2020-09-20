import pandas as pd
import numpy as np

def pprint(d):
	print("---------------------")
	print(d)
	print("---------------------")

def getPeaks(avg,secavg=6):
	newval=0
	rising=False
	out=[]
	avgValues = np.array(avg)
	if len(avgValues.shape)==2:
		avgValues = [item[1] for item in avg]
		offset=avg[0][0]
	else:
		offset=0
	secondavg=getMovingAvg(avgValues,ran=secavg)
	prevval=avgValues[secondavg[0][0]]
	for i in range(secondavg[0][0]+1,len(secondavg)):
		newval=avgValues[i]
		if (prevval>newval and rising==True):
			newval=avgValues[i-1]
			rising=False
			if(newval>secondavg[i][1]):
				out.append([offset+i-1,newval])
		if prevval<newval:
			rising=True
		prevval=newval
	return out

def getVally(avg,secavg=6):
	newval=0
	rising=False
	out=[]
	avgValues = np.array(avg)
	if len(avgValues.shape)==2:
		avgValues = [item[1] for item in avg]
		offset=avg[0][0]
	else:
		offset=0
	secondavg=getMovingAvg(avgValues,ran=secavg)
	prevval=avgValues[secondavg[0][0]]
	for i in range(secondavg[0][0]+1,len(secondavg)):
		newval=avgValues[i]
		if (prevval<newval and rising==True):
			newval=avgValues[i-1]
			rising=False
			if(newval<secondavg[i][1]):
				out.append([offset+i-1,newval])
		if prevval>newval:
			rising=True
		prevval=newval
	return out

def getMovingAvg(data,ran=4):
	out=[]
	for i in range(ran,len(data)):
		avgval=np.sum(data[i-ran:i])/(ran)
		out.append([i-ran//2,avgval])
	return out

def determineTrend(data,offset=30,avgnum=50):
	avg=getMovingAvg(data,avgnum)
	if(offset>=len(avg)):
		offset=len(avg)-1
	return (avg[-1][1]-avg[-(1+offset)][1])*1000


#return lowest high, highest high,highest low ,lowest low
def getLowHigh(peaks,vally):
	hh=[-1,-99999999]
	lh=[-1,99999999]
	hl=[-1,-99999999]
	ll=[-1,99999999]
	for p in peaks:
		if p[1]>hh[1]:
			hh=[p[0],p[1]]
		if p[1]<lh[1]:
			lh=[p[0],p[1]]

	for v in vally:
		if v[1]>hl[1]:
			hl=[v[0],v[1]]
		if v[1]<ll[1]:
			ll=[v[0],v[1]]
	return hh,lh,hl,ll

def getDeviation(avg,val):
	avgnp=np.array(avg)
	val=np.array(val)
	return np.sqrt(np.sum(np.square(avgnp[:,1]-val[2*int(avgnp[0][0]):]))/len(avgnp))