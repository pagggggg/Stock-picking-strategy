import twstock
from twstock import Stock
import numpy as np

def long_strategy(stockid):

    stock = twstock.Stock(stockid)


    price20 = stock.price[-20:]     #月
    price100 = stock.price[-100:]    #年
    ma_p20=np.mean(price20)
    ma_p100=np.mean(price100)

    if ma_p20>=ma_p100:
        #print("可觀察，建議靠近月均價買進較佳，月線價格："+str(ma_p20))
        str1="符合20週均線大於20日均線之策略，(建議價格靠近20週均價買進："+str("%.2f" % ma_p20)+")"
        return str1
    else:
        #print("不符合上漲趨勢，不建議買進！")
        str1="不符合20週均線大於20日均線之策略，不建議買進"
        return str1
