# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from pymongo import  MongoClient


# read datas from apps
# df = pd.read_excel(r'/media/juner/0003734A0009FB81/git/scrapy-learn/wandoujia/app.xlsx',encoding='utf-8')
df = pd.read_excel(r'H:\git\scrapy-learn\wandoujia\app.xlsx',encoding='utf-8')
df_dict = df.apply(dict,axis=1)


# create connections
connection=MongoClient('127.0.0.1',27017)


# chose db
db = connection.test

# chose collections
collection = db.wandoujia_app

# write datas to mongodb
collection.insert(df_dict)

