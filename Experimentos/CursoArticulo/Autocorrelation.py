# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:25:56 2022

@author: abz1e14
"""
from pandas import read_excel
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf
series1 = read_excel('CementProduction.xls', sheetname='Data', header=0,
              index_col=0, parse_dates=True, squeeze=True)
series2 = read_excel('CementProduction.xls', sheetname='SeasonalData', header=0,
                    index_col=0, parse_dates=True, squeeze=True)
series2.plot(title='Seasonal plots building materials time series')
pyplot.show()

plot_acf(series1, title='ACF plot of building materials time series', lags=60)
pyplot.show()

autocorrelation_plot(series1)
pyplot.show()
