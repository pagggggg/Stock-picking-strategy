from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import stock_final as f
import twstock
import short_strategy as ss
import long_strategy as ls
import sendgmail as sg
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


#----------------bsp------------------

@app.route('/bsp/')
def bsp():
    return render_template('bsp.html')

#----------------bsp-best_four_point------------------

@app.route('/best_four_point/', methods=['GET','POST'])#接收html傳來的值
def best_four_point():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
                          #  利用request取得表單欄位值
        return redirect(url_for('stockid', stockid=request.form.get('stockid')))
    #  非POST的時候就會回傳一個空白的模板
    return render_template('best_four_point.html')

@app.route('/best_four_point/<stockid>')
def stockid(stockid):
    f.working(stockid)
    return render_template('best_four_point_complete.html', stockid=stockid)

@app.route('/best_four_point_complete/')
def best_four_point_complete():

    return render_template('best_four_point_complete.html')



#----------------bsp-best_four_point------------------
#----------------bsp-short_strategy------------------
@app.route('/bsp_short_strategy/', methods=['GET','POST'])#接收html傳來的值
def bsp_short_strategy():
    if request.method == 'POST':
                          #  利用request取得表單欄位值

        return redirect(url_for('short_strategy_stockid', stockidshort=request.form.get('stockidshort')))
    return render_template('bsp_short_strategy.html')

@app.route('/bsp_short_strategy/<stockidshort>')
def short_strategy_stockid(stockidshort):
    first_ss=ss.short_strategy(stockidshort)

    return render_template('bsp_short_strategy_complete.html',str=first_ss)

@app.route('/bsp_short_strategy_complete/')
def bsp_short_strategy_complete():

    return render_template('bsp_short_strategy_complete.html')
#----------------bsp-short_strategy------------------
#----------------bsp_long_strategy------------------
@app.route('/bsp_long_strategy/', methods=['GET','POST'])#接收html傳來的值
def bsp_long_strategy():
    if request.method == 'POST':
                          #  利用request取得表單欄位值

        return redirect(url_for('long_strategy_stockid', stockidlong=request.form.get('stockidlong')))
    return render_template('bsp_long_strategy.html')

@app.route('/bsp_long_strategy/<stockidlong>')
def long_strategy_stockid(stockidlong):
    first_sl=ls.long_strategy(stockidlong)

    return render_template('bsp_long_strategy_complete.html',str=first_sl)

@app.route('/bsp_long_strategy_complete/')
def bsp_long_strategy_complete():

    return render_template('bsp_long_strategy_complete.html')
#----------------bsp-short_strategy------------------


#----------------bsp_complete------------------
#----------------dtss------------------

@app.route('/dtss/')
def dtss():
    return render_template('dtss.html')

@app.route('/dtss_first/')
def dtss_first():
    file_dtss_first = open('../dtss/dtss_first/dtss_first_stock_result.txt', 'r')
    first_str=file_dtss_first.read()
    return render_template('dtss_first.html',str=first_str)

@app.route('/dtss_humanity/')
def dtss_humanity():
    file_dtss_humanity = open('../dtss/dtss_humanity/dtss_humanity_result.txt', 'r')
    humanity_str=file_dtss_humanity.read()

    return render_template('dtss_humanity.html',str=humanity_str)


#----------------login------------------

@app.route('/login/', methods=['GET','POST'])
def login():
    #  利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
                          #  利用request取得表單欄位值
            return redirect(url_for('account', account=request.form.get('account')))#還有password的值沒有抓到
    #  非POST的時候就會回傳一個空白的模板
    return render_template('login.html')

@app.route('/login/<account>')
def account(account):
    sg.sendgmail(account)
    return render_template('login_complete.html', account=account)

@app.route('/login_complete/')
def login_complete():

    return render_template('login_complete.html')
#----------------login_complete------------------




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
