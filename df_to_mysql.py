# -*- coding:utf8 -*-

import numpy as np
import pandas as pd
import pymysql
from sqlalchemy import create_engine

host = '127.0.0.1'
port = 3306
db = 'test'
user = 'root'
passwd = '1234'

df = pd.DataFrame(np.arange(12).reshape(3,4))

# engine = create_engine(str(r'mysql+mysqldb://%s:'+'%s'+'@%s/%s' %(user,passwd,host,db)))
engine = create_engine(str(r"mysql+pymysql://%s:" + '%s' + "@%s:%s/%s") % (user, passwd, host, port, db))


try:
    df.to_sql('df_to_mysql',con=engine,if_exists='replace',index=False)
except Exception as e:
    print(e)