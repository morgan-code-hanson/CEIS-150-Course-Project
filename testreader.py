# -*- coding: utf-8 -*-
from stock_class import Stock, DailyData
from datetime import datetime

"""
Created on Mon Aug 15 10:15:43 2022

@author: mo
"""
import pandas as pd
import numpy as np

pdreader = pd.read_csv("MSFT.csv", delimiter = ",", converters= {'Date': pd.to_datetime})
#print(testreader)
counter = 0
columns = ["Date", "Close", "Volume"]
x = 0
#for y in range(0,251):
#   date,price,volume = (pdreader["Date"][y], pdreader["Close"][y], pdreader["Volume"][y])
#  daily_data = DailyData(datetime.strptime(date,"%y-%m-%d"),float(price),float(volume))
#
print(type(pdreader["Date"][0]))