import twstock
from pprint import pprint
#找出前一天成交量>5000張的股票，並匯入for_dtss_first.txt中
def stock_realtime_first():
    #print('--------------------------TWSE--------------------------')
    def get_stock_num_list_TW(filename):
        try:
            with open(filename) as stocks:
                raw_data = stocks.read()
            stock_nums = raw_data.strip().split(',')
            return stock_nums
        except:
            print(filename, '讀取錯誤')

    stock_nums = get_stock_num_list_TW('TWSEstocknumber.txt')
    #print(stock_nums)
    #print(len(stock_nums))

    def get_stock_dict_TW(stock_nums):
        stock_dict = {}
        for start in range(0, len(stock_nums), 100): # Search 100 stocks each time，可以調成10次來檢測是不是有問題（5/3的凌晨）
            try:
                end = start + 100 if (start + 100) < len(stock_nums) else len(stock_nums)
                return_dict = twstock.realtime.get(stock_nums[start:end])
                #print(stock_nums[start:end])#測試是不是證交所網頁的問題，凌晨五點會怪怪的（5/3的凌晨）
                if return_dict['success']:
                    stock_dict.update(return_dict)
                    del stock_dict['success'] # remove this bool object to keep the stock_dict clean
                else:
                    print('Error')
            except:
                i=3
        return stock_dict

    stock_dict = get_stock_dict_TW(stock_nums)

    #print(stock_dict)#印出所有realtime的資料
    def get_stock_last_price_TW(stock_dict):
        f = open('for_dtss_first_TW.txt', 'w')
        stock_last_price = {}
        for stock_num, stock in stock_dict.items():
            if stock['success']:
                try:#解決當天沒有交易的股票5/2
                    last_price = float(stock['realtime']['latest_trade_price'])
                    total_volume = float(stock['realtime']['accumulate_trade_volume'])
                    if total_volume>5000 and 10< last_price and total_volume!=None :

                    #stock_last_price[stock_num] = last_price,total_volume#將價格,成交量加在股號後面，ＥＸ： '6488': (337.0, 7163.0)
                    #print('股號',stock_num,'現價',last_price,'成交量',total_volume)
                        f = open('for_dtss_first_TW.txt', 'a')
                        f.write(stock_num+',')#可以存入，但最後會多一個逗點
                    else:
                        i=1
                #print(stock_num, last_price,total_volume)
                except:
                    i=2
            else:
                print('Stock', stock_num, 'fail')
        return stock_last_price

    stock_last_price = get_stock_last_price_TW(stock_dict)
    f = open('for_dtss_first_TW.txt', 'a')
    f.write('9958')#為了要讓結尾不是逗點5/3
    #print(stock_last_price)

    ##print('--------------------------OTC--------------------------')

    def get_stock_num_list_OTC(filename):
        try:
            with open(filename) as stocks:
                raw_data = stocks.read()
            stock_nums = raw_data.strip().split(',')
            return stock_nums
        except:
            print(filename, '讀取錯誤')

    stock_nums = get_stock_num_list_OTC('TWOTCstocknumber.txt')
    #print(stock_nums)
    #print(len(stock_nums))

    def get_stock_dict_OTC(stock_nums):
        stock_dict = {}
        for start in range(0, len(stock_nums), 100): # Search 100 stocks each time，可以調成10次來檢測是不是有問題（5/3的凌晨）
            try:
                end = start + 100 if (start + 100) < len(stock_nums) else len(stock_nums)
                return_dict = twstock.realtime.get(stock_nums[start:end])
                #print(stock_nums[start:end])#測試是不是證交所網頁的問題，凌晨五點會怪怪的（5/3的凌晨）
                if return_dict['success']:
                    stock_dict.update(return_dict)
                    del stock_dict['success'] # remove this bool object to keep the stock_dict clean
                else:
                    print('Error')
            except:
                i=3
        return stock_dict

    stock_dict = get_stock_dict_OTC(stock_nums)

    #print(stock_dict)#印出所有realtime的資料

    def get_stock_last_price_OTC(stock_dict):
        f = open('for_dtss_first_OTC.txt', 'w')
        stock_last_price = {}
        for stock_num, stock in stock_dict.items():
            if stock['success']:
                try:#解決當天沒有交易的股票5/2
                    last_price = float(stock['realtime']['latest_trade_price'])
                    total_volume = float(stock['realtime']['accumulate_trade_volume'])
                    if total_volume>200 and 10< last_price <100 and total_volume!=None :

                    #stock_last_price[stock_num] = last_price,total_volume#將價格,成交量加在股號後面，ＥＸ： '6488': (337.0, 7163.0)
                    #print('股號',stock_num,'現價',last_price,'成交量',total_volume)
                        f = open('for_dtss_first_OTC.txt', 'a')
                        f.write(stock_num+',')#可以存入，但最後會多一個逗點
                    else:
                        i=1
                #print(stock_num, last_price,total_volume)
                except:
                    i=2
            else:
                print('Stock', stock_num, 'fail')
        return stock_last_price

    stock_last_price = get_stock_last_price_OTC(stock_dict)
    f = open('for_dtss_first_OTC.txt', 'a')
    f.write('9962')
    print('stock_realtime_first完成')
