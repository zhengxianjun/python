# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import pymysql
from sqlalchemy import create_engine

host = '127.0.0.1'
port = 3306
db = 'test'
user = 'root'
passwd = '1234'

# df = pd.DataFrame(np.arange(12).reshape(4,3))
df = pd.read_excel(r'/media/juner/0003734A0009FB81/git/scrapy-learn/wandoujia/app.xlsx',encoding='utf-8')
# print(df.head())


# engine = create_engine(str(r'mysql+mysqldb://%s:'+'%s'+'@%s/%s' %(user,passwd,host,db)))
engine = create_engine(str(r"mysql+pymysql://%s:" + '%s' + "@%s:%s/%s?charset=utf8") % (user, passwd, host, port, db))


try:
    df.to_sql(
        name='wandoujia_apps',
        con=engine,
        if_exists='replace',    # 可选参数 replace append fail
        index=False
        # chunksize=1000  # 按块读取

    )
except Exception as e:
    print(e)