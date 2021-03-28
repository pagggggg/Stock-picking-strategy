import time
import stock_module as m
def working(stockid):
    slist=m.get_setting(stockid)
    cnt=len(slist)

    log1=[]
    log2=[]
    for i in range(cnt):
        log1.append('')
        log2.append('')

    check_cnt=1
    while True:
        for i in range(cnt):                  #走訪每一支個股票
            id, low, high=slist[i]
            name, price=m.get_price(id)#
            print('檢查：',name, '股價：',price, '區間：' ,low, '~' ,high)#
            if price<=low:                                #
                if log1[i]!='買進':                         #
                    m.send_ifttt(name,price,'買進（股價低於'+str(low)+'）')#
                    log1[i]='買進'                         #
            elif price>=high:                            #
                if log1[i]!='賣出':                        #
                    m.send_ifttt(name,price,'賣出（股價高於'+str(high)+'）')#
                    log1[i]='賣出'                          #
            act,why=m.get_best(id)                   #
            if why:                                          #
                if log2[i]!=why:
                    m.send_ifttt(name,price,act+'（'+why+'）')
                    log2[i]=why
        print('-------------------')
        check_cnt-=1
        if check_cnt==0:break
        time.sleep(5)
