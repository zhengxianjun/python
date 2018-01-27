#-*- coding: utf-8 -*-
"""

Title:
author: xjzheng
date:

"""

import pandas as pd
import numpy as np
import datetime



# 计算两个日期之间的工作日数,非天数.
class workDays():
    def __init__(self, start_date, end_date, days_off=None) -> object:
        """days_off:休息日,默认周六日, 以0(星期一)开始,到6(星期天)结束, 传入tupple
        没有包含法定节假日,
        """
        self.start_date = start_date
        self.end_date = end_date
        self.days_off = days_off
        if self.start_date > self.end_date:
            self.start_date, self.end_date = self.end_date, self.start_date
        if days_off is None:
            self.days_off = [5, 6]
        # 每周工作日列表
        self.days_work = [x for x in range(7) if x not in self.days_off]
        self.holidays = [
            datetime.date(2018,1,1),
            datetime.date(2017,10,1),
            datetime.date(2017, 10, 2),
            datetime.date(2017, 10, 3),
            datetime.date(2017, 10, 4),
            datetime.date(2017, 10, 5),
            datetime.date(2017, 10, 6),
            datetime.date(2017, 10, 7),
            datetime.date(2017, 10, 8)
        ]
        self.weekdayChangeWorkday = [
            datetime.date(2017, 9, 30)
        ]
    def workDays(self):
        """实现工作日的 iter, 从start_date 到 end_date , 如果在工作日内,yield 日期
        """
        tag_date = self.start_date
        while tag_date <= self.end_date:
            if tag_date.weekday() in self.days_work :
                if tag_date not in self.holidays: # 排除工作日为节假日
                    yield tag_date
            if tag_date.weekday() in self.days_off:
                if tag_date in self.weekdayChangeWorkday:
                    yield tag_date
            tag_date += datetime.timedelta(days=1)

    def nWorkDays(self):
        """实现非工作日的 iter, 从start_date 到 end_date , 如果在非工作日内,yield 日期
        """
        tag_date = self.start_date
        while tag_date <= self.end_date:
            if tag_date.weekday() in self.days_off:
                if tag_date not in self.weekdayChangeWorkday: #排除周末调休
                    yield tag_date
            if tag_date.weekday() in self.days_work:
                if tag_date in self.holidays:
                    yield tag_date
            tag_date += datetime.timedelta(days=1)

    def WorkDaysCount(self):
        """工作日统计,返回数字"""
        return len(list(self.workDays()))

    def nWorkDaysCount(self):
        '''非工作日统计，返回数字'''
        return  len(list(self.nWorkDays()))


    def weeksCount(self, day_start=0):
        """统计所有跨越的周数,返回数字
        默认周从星期一开始计算
        """
        day_nextweek = self.start_date
        while True:
            if day_nextweek.weekday() == day_start:
                break
            day_nextweek += datetime.timedelta(days=1)
        # 区间在一周内
        if day_nextweek > self.end_date:
            return 1
        weeks = ((self.end_date - day_nextweek).days + 1) / 7
        weeks = int(weeks)
        if ((self.end_date - day_nextweek).days + 1) % 7:
            weeks += 1
        if self.start_date < day_nextweek:
            weeks += 1
        return weeks

# template
# date1 = datetime.date(2017,10,9)
# date2 = datetime.date(2017,9,30)
# nWorkday = workDays(date1,date2)
# print(nWorkday.nWorkDaysCount())

FilePath = r'C:\Users\q\Desktop\LoanOrderList.xlsx'
data = pd.read_excel(FilePath,sheetname='Sheet1')
data['创建时间']=data['创建时间'].astype('datetime64')
# data['评房时间']=data['评房时间'].astype('datetime64')
data['下户完成时间']=data['下户完成时间'].astype('datetime64')
# data['初审时间']=data['初审时间'].astype('datetime64')
# data['价值认定时间']=data['价值认定时间'].astype('datetime64')
data['审批复核时间']=data['审批复核时间'].astype('datetime64')
data['渠道面签时间']=data['渠道面签时间'].astype('datetime64')
# data['公证完成时间']=data['公证完成时间'].astype('datetime64')
# data['抵押完成时间']=data['抵押完成时间'].astype('datetime64')
data['审查时间']=data['审查时间'].astype('datetime64')
data['放款时间']=data['放款时间'].astype('datetime64')
# print(data.head())
# print(data.dtypes)
data['放款天数'] = workDays(data['放款时间'],data['创建时间']).nWorkDaysCount()