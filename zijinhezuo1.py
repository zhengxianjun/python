# -*- coding: utf-8 -*-
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import pandas as pd
import datetime
from email.mime.text import MIMEText
import pymysql

# 查询语句
sql1 = """
SELECT 
"""


# 连接数据库
def py_conn_db(sql):
    conn = pymysql.connect(
        host='xxx',
        port=3307,
        db='xxx',
        user='xxx',
        passwd='xxx',
        charset='utf8'
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchall()
    cursor.close()

    return result


res_1 = py_conn_db(sql1)

#读取excel文件
file_path = r'123.xlsx'
df = pd.read_excel(file_path)

#设置新的index
df_new = df.set_index('还款日期')

#创建透视表
df_pivot = pd.pivot_table(df_new,index=df_new.index,columns='信托计划',fill_value=0)

#按周统计
df_result = df_pivot.resample('W').sum()

#输出的excel文件名
result_filename = 'repayment of finacing_channel '+datetime.datetime.now().strftime("%Y-%m-%d") + '.xlsx'

#存excel文件
df_result.to_excel(result_filename)

#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.exmail.qq.com'
#163用户名
mail_user = 'zhengxianjun@jindankeji.com'
#密码(部分邮箱为授权码)
mail_pass = 'zLk4xroAZA6VxRDz'
#邮件发送方邮箱地址
sender = 'zhengxianjun@jindankeji.com'
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['zhengxianjun@jindankeji.com']

#设置邮件内容
content = '''
测试邮件
'''

#设置email信息
#邮件内容设置
message = MIMEMultipart()
#邮件主题
message['Subject'] = '中航和天百资金方未来还款统计'
#发送方信息
message['From'] = sender
#接受方信息
message['To'] = receivers[0]
#解决编码问题
message["Accept-Language"] = "zh-CN"
message["Accept-Charset"] = "ISO-8859-1,utf-8"

#邮件内容 纯文本部分
puretext = MIMEText('测试邮件')
message.attach(puretext)

#邮件内容 附件部分
xlsxpart = MIMEApplication(open(result_filename, 'rb').read())
xlsxpart.add_header('Content-Disposition', 'attachment', filename=result_filename)
message.attach(xlsxpart)

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