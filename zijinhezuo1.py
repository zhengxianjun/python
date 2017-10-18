# -*- coding: utf-8 -*-

import pandas as pd
import datetime

file_path = r'H:\git\python\123.xlsx'
df = pd.read_excel(file_path)
df_new = df.set_index('还款日期')
#print(df_new.head())
df_pivot = pd.pivot_table(df_new,index=df_new.index,columns='信托计划',fill_value=0)
print(df_pivot.tail())
df_result = df_pivot.resample('W').sum()

#输出的excel文件名
result_filename = '资金合作还款统计'+datetime.datetime.now().strftime("%Y-%m-%d") + '.xlsx'

#存excel文件
df_result.to_excel(result_filename)

