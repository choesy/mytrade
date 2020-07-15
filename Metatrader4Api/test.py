from webpager import tradedriver
import time
tr =tradedriver()
ordername=tr.place_order("USDJPY","buy",0.01,0,0)
ordername2=tr.place_order("EURUSD","sell",0.01,0,0)
ordername3=tr.place_order("EURUSD","buy",0.01,0,0)

tr.close_orders("all")

