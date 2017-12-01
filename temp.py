#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql

sql1 = "select appcategory from wandoujia_apps limit 10"

# 连接数据库
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

sql_result = py_conn_db(sql1)
for res in sql_result:
    print(sql_result[0])


