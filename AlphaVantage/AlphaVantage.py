from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from alpha_vantage.foreignexchange import ForeignExchange
def getfxdata(alphaVantageKey,our,their,interval):
	data=None
	while data is None:
		try:
			fx = ForeignExchange(key=alphaVantageKey ,output_format='pandas')
			data, meta_data = fx.get_currency_exchange_intraday(our,their,interval=interval, outputsize='full')
		except:
			pass
	return data['4. close']
	
