# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:02:33 2017

@author: q
"""

# 导入模块
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 导入数据
data = pd.read_excel('C:\\Users\\Administrator\\Desktop\\货运.xls')

# 绘图
plt.bar(np.arange(8), data.loc[0,:][1:], 
        color = 'red', alpha = 0.8, label = '铁路', align = 'center')
plt.bar(np.arange(8), data.loc[1,:][1:],  bottom = data.loc[0,:][1:], 
        color = 'green', alpha = 0.8, label = '公路', align = 'center')
plt.bar(np.arange(8), data.loc[2,:][1:],  bottom = data.loc[0,:][1:]+data.loc[1,:][1:], 
        color = 'm', alpha = 0.8, label = '水运', align = 'center')
plt.bar(np.arange(8), data.loc[3,:][1:],  bottom = data.loc[0,:][1:]+data.loc[1,:][1:]+data.loc[2,:][1:], 
        color = 'black', alpha = 0.8, label = '民航', align = 'center')
# 添加轴标签
plt.xlabel('月份')
plt.ylabel('货物量(万吨)')
# 添加标题
plt.title('2017年各月份物流运输量')
# 添加刻度标签
plt.xticks(np.arange(8),data.columns[1:])
# 设置Y轴的刻度范围
plt.ylim([0,500000])

# 为每个条形图添加数值标签
for x_t,y_t in enumerate(data.loc[0,:][1:]):
    plt.text(x_t,y_t/2,'%sW' %(round(y_t/10000,2)),ha='center', color = 'white')

for x_g,y_g in enumerate(data.loc[0,:][1:]+data.loc[1,:][1:]):
    plt.text(x_g,y_g/2,'%sW' %(round(y_g/10000,2)),ha='center', color = 'white') 

for x_s,y_s in enumerate(data.loc[0,:][1:]+data.loc[1,:][1:]+data.loc[2,:][1:]):
    plt.text(x_s,y_s-20000,'%sW' %(round(y_s/10000,2)),ha='center', color = 'white')    

# 显示图例
plt.legend(loc='upper center', ncol=4)
# 显示图形    
plt.show()