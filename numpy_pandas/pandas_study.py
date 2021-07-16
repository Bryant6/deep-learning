# -*-coding:utf-8-*-
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1])
print(s)
dates = pd.date_range('20210715', periods=7)
print(dates)
