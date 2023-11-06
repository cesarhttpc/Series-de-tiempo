# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:15:06 2022

@author: abz1e14
"""
from pandas import read_excel
from matplotlib import pyplot
series = read_excel('MilkProduction.xls',
              sheetname='AdjustedData', header=0,
              index_col=0, parse_dates=True, squeeze=True)  # you can include various other parameters
series.plot()
pyplot.show()
