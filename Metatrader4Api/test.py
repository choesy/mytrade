from webpager import tradedriver
tr =tradedriver()
input("Press Enter to continue...")

tr.authorize_oneclick()


ordername=tr.place_order("USDJPY","buy",0.01,0,0)

print(ordername)
