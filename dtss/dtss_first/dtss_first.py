import twstock
from pprint import pprint
import datetime
import pandas_datareader as pdr
import pandas as pd
import pandas_datareader.data as web
from datetime import timedelta, datetime

def dtss_first():

    print('-------------------------OTC--------------------------')

    def get_stock_num_list_OTC(filename):
        try:
            with open(filename) as stocks:
                raw_data = stocks.read()
            stock_nums = raw_data.strip().split(',')
            return stock_nums
        except:
            print(filename, '讀取錯誤')

    stock_nums = get_stock_num_list_OTC('for_dtss_first_OTC.txt')
    #print(stock_nums)
    #print(len(stock_nums))#有幾個

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

    def get_result_OTC(stock_dict):
        f = open('dtss_first_stock_result.txt', 'w')
        stock_result_TW = {}
        for stock_num, stock in stock_dict.items():


            yesterday = datetime.today() + timedelta(-1)#找出昨天週末會比較麻煩
            yesterday_format = yesterday.strftime('%Y-%m-%d')

            today= datetime.today()
            today_format = today.strftime('%Y-%m-%d')
            #print("昨天",yesterday_format,'今天',today_format)
            try:
                data1 = pdr.DataReader(str(stock_num)+'.TWO', 'yahoo', yesterday_format, yesterday_format)
                y = float(data1['Close'])#找出昨天收盤價
                yesterday_close_price = "%.2f" % y#四捨五入小數點第二位

                #print(yesterday_close_price)
                data2 = pdr.DataReader(str(stock_num)+'.TWO', 'yahoo', today_format, today_format)#星期天會沒資料
                t =float(data2['Open'])#找出今天的開盤價
                today_open_price ="%.2f" % t#四捨五入小數點第二位


                p=y-t
                if p>0:
                    a=p/y
                    #print(a)
                    if 0.02<a<0.05:
                        b=a*100
                        c="%.2f" % b
                        print('股號',stock_num,'昨天收盤價',yesterday_close_price,'今天開盤價',today_open_price,'下跌',c+'%')
                        f = open('dtss_first_stock_result.txt', 'a')
                        f.write('{[ 股號：'+stock_num+'  昨收：'+yesterday_close_price+'  今開：'+today_open_price+' 下跌 '+c+'%'+' ]}\n')
                        #stock_result_TW[stock_num] =yesterday_close_price,today_open_price

                    else:
                        i=0
                else:
                    i=1
            except:
                i=1
        return stock_result_TW

    stock_result_OTC = get_result_OTC(stock_dict)
    #print(stock_result_OTC)
    print('-------------------------TWSE-------------------------')
    def get_stock_num_list_TW(filename):
        try:
            with open(filename) as stocks:
                raw_data = stocks.read()
            stock_nums = raw_data.strip().split(',')
            return stock_nums
        except:
            print(filename, '讀取錯誤')

    stock_nums = get_stock_num_list_TW('for_dtss_first_TW.txt')
    #print(stock_nums)
    #print(len(stock_nums))#有幾個

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

    def get_result_TW(stock_dict):
        stock_result_TW = {}
        for stock_num, stock in stock_dict.items():


            yesterday = datetime.today() + timedelta(-1)#找出昨天
            yesterday_format = yesterday.strftime('%Y-%m-%d')
            today= datetime.today()
            today_format = today.strftime('%Y-%m-%d')

            try:

                data1 = pdr.DataReader(str(stock_num)+'.TW', 'yahoo', yesterday_format, yesterday_format)
                y = float(data1['Close'])#找出昨天收盤價
                yesterday_close_price = "%.2f" % y#四捨五入小數點第二位


                data2 = pdr.DataReader(str(stock_num)+'.TW', 'yahoo', today_format, today_format)
                t =float(data2['Open'])#找出今天的開盤價
                today_open_price ="%.2f" % t#四捨五入小數點第二位


                #print('股號',stock_num,'昨天收盤價',yesterday_close_price,'今天開盤價',today_open_price)
                p=y-t
                if p>0:
                    a=p/y
                    #print(a)
                    if 0.02<a<0.035:
                        b=a*100
                        c="%.2f" % b
                        print('股號',stock_num,'昨天收盤價',yesterday_close_price,'今天開盤價',today_open_price,'下跌',c+'%')
                        f = open('dtss_first_stock_result.txt', 'a')
                        f.write('{[ 股號：'+stock_num+'  昨收：'+yesterday_close_price+'  今開：'+today_open_price+' 下跌 '+c+'%'+' ]}\n')
                        #stock_result_TW[stock_num] = ' 昨收：'+str(yesterday_close_price)+' 今開：'+str(today_open_price)
                    else:
                        i=0
                else:
                    i=1
            except:
                print(stock_num,'Error')
        return stock_result_TW

    stock_result_TW = get_result_TW(stock_dict)
    #print(stock_result_TW)
