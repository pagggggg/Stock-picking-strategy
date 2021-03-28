import smtplib
from email.mime.text import MIMEText


def sendgmail(gmailid):
    gmail_user = 'pagggggg3206@gmail.com'
    gmail_password = 'gg14250.250.41' # your gmail password

    msg = MIMEText('感謝您選擇我們，目前所以策略都可免費使用，點選 http://4fcefad7.ngrok.io 回到策略網頁。')
    msg['Subject'] = '智慧選股系統'
    msg['From'] = gmail_user
    msg['To'] = gmailid

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()
    f = open('gmailID.txt','a')
    f.write(gmailid+',')
    #print('Email sent!')
