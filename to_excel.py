# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:50:45 2017

@author: q
"""

# coding:utf8


import xlwt
import pymysql

def export(outputpath):
    conn = pymysql.connect(
            host='192.168.100.xxx',
            port=3306,
            db='fh_app_tmp2',
            user='xx',
            passwd='xx',
            charset='utf8'
        )
    cursor = conn.cursor()
    #sql语句
    sql1 = '''
    SELECT 
    '''
    
    count = cursor.execute(sql1)

    # 重置游标的位置
    cursor.scroll(0,mode='absolute')
    # 搜取所有结果
    results = cursor.fetchall()

    # 获取MYSQL里面的数据字段名称
    fields = cursor.description
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('table_1',cell_overwrite_ok=True)

    # 写上字段信息
    for field in range(0,len(fields)):
        sheet.write(0,field,fields[field][0])

    # 获取并写入数据段信息
    row = 1
    col = 0
    for row in range(1,len(results)+1):
        for col in range(0,len(fields)):
            sheet.write(row,col,u'%s'%results[row-1][col])

    workbook.save(outputpath)


# 结果测试
if __name__ == "__main__":
    export(r'C:\Users\q\Desktop\datetest.xls')
           
   