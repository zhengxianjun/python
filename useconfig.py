#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# read(filename) 直接读取ini文件内容
# sections() 得到所有的section，并以列表的形式返回
# options(section) 得到该section的所有option
# items(section) 得到该section的所有键值对
# get(section,option) 得到section中option的值，返回为string类型
# getint(section,option) 得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。
# 2）写入配置文件
# add_section(section) 添加一个新的section
# set( section, option, value) 对section中的option进行设置，需要调用write将内容写入配置文件。

import configparser
import pymysql

cf = configparser.ConfigParser()

cf.read(filenames='dbconfig.ini')

se = cf.sections()
op = cf.options('db_mysql')
item = cf.items('db_mysql')
values = cf.get('db_mysql','db_mysql_user')
print(se)

print(op)
print(item)
print(values)

