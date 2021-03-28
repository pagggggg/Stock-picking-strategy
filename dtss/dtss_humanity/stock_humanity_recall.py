import twstock
import time
from pprint import pprint
import random
import numpy as np
#找出前一天成交量>5000張的股票，並匯入for_dtss_first.txt中





def get_stock_num_list_TW(filename):
    try:
        with open(filename) as stocks:
            raw_data = stocks.read()
        stock_nums = raw_data.strip().split(',')
        return stock_nums
    except:
        print(filename, '讀取錯誤')

stock_nums = get_stock_num_list_TW('TWstocknumber.txt')

def get_stock_dict_TW(stock_nums):
    stock_dict = {}
    for start in range(0, len(stock_nums), 100): # Search 100 stocks each time，可以調成10次來檢測是不是有問題（5/3的凌晨）
        end = start + 100 if (start + 100) < len(stock_nums) else len(stock_nums)
        return_dict = twstock.realtime.get(stock_nums[start:end])
        #print(stock_nums[start:end])#測試是不是證交所網頁的問題，凌晨五點會怪怪的（5/3的凌晨）
        if return_dict['success']:
            stock_dict.update(return_dict)
            del stock_dict['success'] # remove this bool object to keep the stock_dict clean
        else:
            print('Error')
    return stock_dict

stock_dict = get_stock_dict_TW(stock_nums)
#print(stock_dict)#印出所有realtime的資料


#print(stock_last_price)
#計算均價
stock_avg_price = {}
def get_stock_avg_price_list(stock_dict):


    for stock_num, stock in stock_dict.items():#先宣告dictionary中的list
    #print(stock)
        if stock['success']:
            try:#解決當天沒有交易的股票5/2
                stock_avg_price[stock_num]=list()# dictionary中包list（5/6）
                #print('股號 ',stock_num,'現價  ',last_price,'均價  ',avg_price,'成交量',total_volume,'單量  ',trade_volume)
            except:
                i=0

        else:
            print('Stock', stock_num, 'fail')

stock_avg_price_list=get_stock_avg_price_list(stock_dict)
print("均價list建立成功")














def stock_realtime_humanity():
    def get_stock_num_list_TW(filename):
        try:
            with open(filename) as stocks:
                raw_data = stocks.read()
            stock_nums = raw_data.strip().split(',')
            return stock_nums
        except:
            print(filename, '讀取錯誤')

    stock_nums = get_stock_num_list_TW('TWstocknumber.txt')
    #print(stock_nums)
    #print(len(stock_nums))

    def get_stock_dict_TW(stock_nums):
        stock_dict = {}
        for start in range(0, len(stock_nums), 100): # Search 100 stocks each time，可以調成10次來檢測是不是有問題（5/3的凌晨）
            end = start + 100 if (start + 100) < len(stock_nums) else len(stock_nums)
            return_dict = twstock.realtime.get(stock_nums[start:end])
            #print(stock_nums[start:end])#測試是不是證交所網頁的問題，凌晨五點會怪怪的（5/3的凌晨）
            if return_dict['success']:
                stock_dict.update(return_dict)
                del stock_dict['success'] # remove this bool object to keep the stock_dict clean
            else:
                print('Error')
        return stock_dict

    stock_dict = get_stock_dict_TW(stock_nums)

    #print(stock_dict)#印出所有realtime的資料
    stock_data = {}
    def stock_data(stock_dict):
        f = open('for_dtss_humanity.txt', 'w')
        stock_data = {}
        for stock_num, stock in stock_dict.items():
            if stock['success']:
                try:#解決當天沒有交易的股票5/2
                    last_price = float(stock['realtime']['latest_trade_price'])
                    s=random.randint(0,99)#以亂數代替股價
                    stock_avg_price[stock_num].append(last_price)#可以重複加入list，#可以重複加入list，可以所有股票，應該是可以更新報價（5/6）
                    a=np.mean(stock_avg_price[stock_num])#有均值
                    avg="%.2f" % a
                    total_volume = float(stock['realtime']['accumulate_trade_volume'])
                    trade_volume = float(stock['realtime']['trade_volume'])
                    high_price = float(stock['realtime']['high'])
                    open_price = float(stock['realtime']['open'])

                    z=(high_price-open_price)/open_price#最高價與開盤價的差距
                    f=(high_price-last_price)/last_price#最高價與收盤價的差距
                    #g=(last_price-a)/a#使訊號出現在均價的上下1%中(5/8)
                    if 1500<total_volume<20000 and 10<last_price<100 and total_volume !=None and 0.03<f and 0.025<z<0.065:# and -0.01<g<0.015:#從早上開執行
                        #stock_last_price[stock_num] = last_price,total_volume#將價格,成交量加在股號後面，ＥＸ： '6488': (337.0, 7163.0)
                        #print('股號',stock_num,'現價',last_price,'成交量',total_volume)
                        print('股價',stock_num,'\n''現價',last_price,'均價',a,'總成交量',total_volume,'單量',trade_volume)
                        f = open('for_dtss_humanity.txt', 'a')
                        f.write(stock_num+',')#可以存入，但最後會多一個逗點
                    else:
                        i=1

                except:
                    i=0

            else:
                print('Stock', stock_num, 'fail')
        return stock_data

    stock_data = stock_data(stock_dict)


print('人性當沖回測')
check_cnt=1 #9:00～1:30的次數
while True:
    s=stock_realtime_humanity()
    print("----------------------------------next----------------------------------")
    #print(stock_data)

    check_cnt-=1
    if check_cnt==0:break
    time.sleep(4)
