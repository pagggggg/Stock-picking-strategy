import twstock
from twstock import Stock
import numpy as np

def short_strategy(stockid):

    stock = twstock.Stock(stockid)

    price5 = stock.price[-5:]       # 近五日之收盤價
    price20 = stock.price[-20:]     #月
    price60 = stock.price[-60:]    #季
    price240 = stock.price[-240:]    #年
    ma_p5=np.mean(price5)
    ma_p20=np.mean(price20)
    ma_p60=np.mean(price60)
    ma_p240=np.mean(price240)

    m1=(ma_p20-ma_p5)/ma_p20
    m3=(ma_p60-ma_p5)/ma_p60

    if ma_p60<ma_p20 :

        #print("可觀察，建議靠近月均價買進較佳，月線價格："+str(ma_p20))
        str1="可觀察，建議靠近月均價買進較佳，月線價格："+str("%.2f" % ma_p20)
        return str1
    elif ma_p240<ma_p60<ma_p20 and 0.01>r:
        #print("現價過高，不建議買進，應靠近月均價買進較佳")
        str1="現價過高，不建議買進，應靠近月均價買進較佳"
        return str1
    elif ma_p240>ma_p60>ma_p5>ma_p20:
        #print("尚未過季線壓力，建議再等待！")
        str1="尚未過季線壓力，建議再等待！"
        return str1
    elif ma_p240>ma_p60 and ma_p5>ma_p20 and ma_p60>ma_p20 and -0.1<r<0.1:
        #print("股價接近季線，建議靠近月均價買進較佳，季線價格："+str(ma_p60))
        str1="股價接近季線，建議靠近月均價買進較佳，季線價格："+str("%.2f" % ma_p60)
        return str1
    else:
        #print("不符合上漲趨勢，不建議買進！")
        str1="不符合上漲趨勢，不建議買進！"
        return str1
