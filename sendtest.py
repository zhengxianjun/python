# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:55:09 2017

@author: q

抓取数据，并发送邮件
"""

import smtplib
import pymysql
import time
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.exmail.qq.com'  
#163用户名
mail_user = 'zhengxianjun@jindankeji.com'  
#密码(部分邮箱为授权码) 
mail_pass = 'pwd'   
#邮件发送方邮箱地址
sender = 'zhengxianjun@jindankeji.com'  
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['zhengxianjun@jindankeji.com']  

#查询语句
sql1 = """
SELECT 
"""



#连接数据库
def py_conn_db(sql):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        db='test',
        user='root',
        passwd='1234',
        charset='utf8'
        )
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    cursor.close()
    
    return result

res_1 = py_conn_db(sql1)

#设置邮件内容
content_0 = "截止到%s\n" %time.strftime('%Y-%m-%d',time.localtime(time.time()))
content_1 = "%s: %s/%s\n" %(res_1[0][2],res_1[0][1],res_1[0][0])
content_2 = "%s: %s/%s" %(res_1[1][2],res_1[1][1],res_1[1][0])
content = content_0+content_1+ content_2




#设置email信息
#邮件内容设置
message = MIMEText(content,'plain','utf-8')
#邮件主题       
message['Subject'] = '中航和天百资金方存量数据' + time.strftime('%Y-%m-%d',time.localtime(time.time()))
#发送方信息
message['From'] = sender 
#接受方信息     
message['To'] = receivers[0] 

#登录并发送邮件
try:
    smtpObj = smtplib.SMTP() 
    #连接到服务器
    smtpObj.connect(mail_host,25)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass) 
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string()) 
    #退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误