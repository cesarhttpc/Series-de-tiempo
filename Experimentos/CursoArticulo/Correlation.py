# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:16:04 2022

@author: abz1e14
"""
from pandas import read_excel
import numpy as np
series1 = read_excel('JapaneseCars.xls', sheet_name='Data', usecols = [0], header=0,
                     squeeze=True, dtype=float)
series2 = read_excel('JapaneseCars.xls', sheet_name='Data', usecols=[1], header=0,
                     squeeze=True, dtype=float)
correlval=np.corrcoef(series1, series2)
correlval=correlval[1,0]
print(correlval)
