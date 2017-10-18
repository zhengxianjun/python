import pandas as pd
df = pd.read_csv('date.csv', header=None)
print(df.head(2))
df.columns = ['date','number']
df['date'] = pd.to_datetime(df['date']) #将数据类型转换为日期类型
df = df.set_index('date') # 将date设置为index
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(type(df))
print(df.index)
print(type(df.index))
s = pd.Series(df['number'], index=df.index)
print(type(s))
s.head(2)
print('---------获取2013年的数据-----------')
print(df['2013'].head(2)) # 获取2013年的数据
print(df['2013'].tail(2)) # 获取2013年的数据
print('---------获取2016至2017年的数据-----------')
print(df['2016':'2017'].head(2))  #获取2016至2017年的数据
print(df['2016':'2017'].tail(2))  #获取2016至2017年的数据
print('---------获取某月的数据-----------')
print(df['2013-11']) # 获取某月的数据
# 按日期筛选数据
print('---------获取具体某天的数据-----------')
# 获取具体某天的数据
print(s['2013-11-06'])

# 获取具体某天的数据，用datafrme直接选取某天时会报错，而series的数据就没有问题
# print(df['2013-11-06'])

#可以考虑用区间来获取某天的数据
print(df['2013-11-06':'2013-11-06'])
# dataframe的truncate函数可以获取某个时期之前或之后的数据，或者某个时间区间的数据
# 但一般建议直接用切片（slice），这样更为直观，方便
print('---------获取某个时期之前或之后的数据-----------')
print('--------after------------')
print(df.truncate(after = '2013-11'))
print('--------before------------')
print(df.truncate(before='2017-02'))
df_period = df.to_period('M') #按月显示，但不统计
print(type(df_period))

print(type(df_period.index))
# 请注意df.index的数据类型是DatetimeIndex；
# df_peirod的数据类型是PeriodIndex

print(df_period.head())
print(df.to_period('Q').head()) #按季度显示，但不统计
print(df.to_period('A').head()) #按年度显示，但不统计
df_period.index.asfreq('A') # 'A'默认是'A-DEC',其他如'A-JAN'
df_period.index.asfreq('A-JAN') # 'A'默认是'A-DEC',其他如'A-JAN'
df_period.index.asfreq('Q') # 'Q'默认是'Q-DEC',其他如“Q-SEP”，“Q-FEB”
df_period.index.asfreq('Q-SEP') # 可以显示不同的季度财年，“Q-SEP”，“Q-FEB”
# df_period.index = df_period.index.asfreq('Q-DEC') # 可以显示不同的季度财年，“Q-SEP”，“Q-FEB”
# print(df_period.head())

df_period.index.asfreq('M') # 按月份显示
df_period.index.asfreq('B', how='start') # 按工作日期显示
df_period.index.asfreq('B', how='end') # 按工作日期显示
print(df.resample('w').sum().head())
# “w”，week
print(df.resample('M').sum().head())
# "MS"是每个月第一天为开始日期, "M"是每个月最后一天
print(df.resample('Q').sum().head())
# "QS"是每个季度第一天为开始日期, "Q"是每个季度最后一天
print(df.resample('AS').sum())
# "AS"是每年第一天为开始日期, "A是每年最后一天
print(df.resample('AS').sum().to_period('A'))# 按年统计并显示
print(df.resample('Q').sum().to_period('Q').head())# 按季度统计并显示

