# %%
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from PythonTsa.plot_acf_pacf import acf_pacf_fig

from statsmodels.tsa.arima.model import ARIMA
# for statsmodels 0.13.0 and later, see the last code below
from PythonTsa.LjungBoxtest import plot_LB_pvalue
from PythonTsa.datadir import getdtapath

# %%
# dtapath=getdtapath()
nao=pd.read_csv('nao.csv', header=0)
timeindex=pd.date_range('1950-01', periods=len(nao),freq='M')
nao.index=timeindex
naots=nao['index']

# %%
# automatically become a Series, see below
type(nao)
type(naots)
naots.plot(); plt.show()
acf_pacf_fig(naots, both=True, lag=48); plt.show()
sm.tsa.stattools.kpss(naots, regression="c", nlags=50)
# %%
ar1=ARMA(naots, order=(1,0)).fit(trend='c', disp=False)
print(ar1.summary())
