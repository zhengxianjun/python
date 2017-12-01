#-*- coding: utf-8 -*-
"""

Title:
author: xjzheng
date:

"""
import json
import numpy as np
import pandas  as pd


filename = r'C:\Users\q\Desktop\jdfq_yuqi.json'
with open(filename) as f:
    pop_data = json.loads(f.read())


data = pd.DataFrame(pop_data)
data.to_excel('result.xls')