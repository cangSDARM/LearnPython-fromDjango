import smtplib
from email.mine.text import MIMEText
from email.utils import formataddr

# 邮件服务
def emailSend(email_list, contents, subject="Title"):    #(收件方列表, 内容, 邮件标题)
    msg = MIMEText(contents, 'plain', 'utf-8')
    msg['From'] = formataddr(['发送方称号', '发送邮箱@126.com'])
    msg['Subject'] = subject

    server = smtplib.SMTP('SMTP服务器域名', 25)   #邮箱需开启SMTP服务, 25端口
    server.login('发送邮箱@126.com', 'password')
    server.sendmail('发送邮箱@126.com', email_list, contents)
    server.quit

import requests
#手机收发服务
def phoneSend():
    rep = requests.get('')  #服务商要求GET请求的格式
    result = rep.text     #返回