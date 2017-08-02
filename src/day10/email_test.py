#coding: utf-8  
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import datetime
  
sender = '438090154@qq.com'
receiver = ['liaozhenhua@hust.edu.cn', '1253684078@qq.com']
smtpserver = 'smtp.qq.com' 
username = '438090154@qq.com'
password = 'liao111'
  
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('亲爱的老婆！！！', 'plain', 'utf-8')
message['From'] = Header("老公", 'utf-8')
message['To'] =  Header("亲爱的老婆", 'utf-8')

now_ = datetime.datetime.now().strftime("%Y-%m-%d")
subject = '亲爱的，今天是' + now_ + '，好好学习哦！！！'
message['Subject'] = Header(subject, 'utf-8')

#/home/ubuntu/python_email/email_test.py

if __name__ == '__main__':
    try:
        smtp = smtplib.SMTP()  
        smtp.connect(smtpserver)
        smtp.login(username, password)  
        smtp.sendmail(sender, receiver, message.as_string())
        smtp.quit()
        print('邮件发送成功')
    except:
        print('error:无法发送邮件')

