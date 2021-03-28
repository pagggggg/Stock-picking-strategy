import twstock
from pprint import pprint
#找出前一天成交量>5000張的股票，並匯入for_dtss_first.txt中
    #print(stock_dict)#印出所有realtime的資料
stock=twstock.realtime.get('8087')
last_price = float(stock['realtime']['latest_trade_price'])
total_volume = float(stock['realtime']['accumulate_trade_volume'])
print(last_price)
