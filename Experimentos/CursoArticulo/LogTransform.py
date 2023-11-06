# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:08:38 2022

@author: abz1e14
"""
from pandas import read_excel
from pandas import DataFrame
from numpy import log
from matplotlib import pyplot
series = read_excel('Electricity.xls',
              sheetname='Data', header=0,
              index_col=0, parse_dates=True, squeeze=True)
dataframe = DataFrame(series.values)
dataframe.columns = ['electricity']
dataframe['electricity'] = log(dataframe['electricity'])
pyplot.figure(1)
# line plot
pyplot.subplot(211)
pyplot.plot(dataframe['electricity'])
# histogram
pyplot.subplot(212)
pyplot.hist(dataframe['electricity'])
pyplot.show()
