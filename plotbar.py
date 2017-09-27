# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:04:47 2017

@author: q
"""

#how to use maplotlib to make Bar chart

#导入绘图包 
import matplotlib.pyplot as plt 

#构建数据
GDP = [123456.7,123464.9,456468.32,354525.5]

#中文乱码的处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#绘图
plt.bar(range(4),GDP,align ='center',color='steelblue',alpha=0.8)

#添加轴标签
plt.ylabel('GDP')

#添加标题
plt.title('四个城市GDP')

#添加刻度标签
plt.xticks(range(4),['北京市','上海市','天津市','重庆市'])

#设置Y轴刻度范围
plt.ylim([100000,500000])

#为每个图形添加数值标签
for x,y in enumerate(GDP):
    plt.text(x,y,'%s' %round(y,1),ha='center')
#显示图形
plt.show()

