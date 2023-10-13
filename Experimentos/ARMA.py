
















'''
https://www.statsmodels.org/devel/examples/notebooks/generated/tsa_arma_0.html#Sunspots-Data

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.tsa.arima.model import ARIMA

from statsmodels.graphics.api import qqplot

print(sm.datasets.sunspots.NOTE)

# %%
dta = sm.datasets.sunspots.load_pandas().data

dta.index = pd.Index(sm.tsa.datetools.dates_from_range("1700", "2008"))
dta.index.freq = dta.index.inferred_freq
del dta["YEAR"]

dta.plot(figsize=(12, 8))

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)


# %%
arma_mod20 = ARIMA(dta, order=(2, 0, 0)).fit()
print(arma_mod20.params)


arma_mod30 = ARIMA(dta, order=(3, 0, 0)).fit()


print(arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic)


# %%

sm.stats.durbin_watson(arma_mod30.resid.values)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax = arma_mod30.resid.plot(ax=ax)
'''