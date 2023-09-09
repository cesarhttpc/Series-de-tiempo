import numpy as np 
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt  
import seaborn as sns    
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("Tarea1/monthly.csv")

df1 = df.loc[(df['Source'] == 'GCAG')]
df2 = df.loc[(df['Source'] == 'GISTEMP')]
print(df1)


# Descomposición aditiva para toda la base de datos
additive_decomposition1 = seasonal_decompose(df['Mean'], model='additive', period=12) 

plt.rcParams.update({'figure.figsize': (16,12)})


additive_decomposition1.plot().suptitle('Tendencia, Estacionalidad y Errores', fontsize=10)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# plt.show()


# Descomposición aditiva para los datos de la fuente GCAG
additive_decomposition2 = seasonal_decompose(df1['Mean'], model='additive', period=12) 

plt.rcParams.update({'figure.figsize': (16,12)})


additive_decomposition2.plot().suptitle('Tendencia, Estacionalidad y Errores', fontsize=10)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# plt.show()


# Descomposición aditiva para los datos de la fuente GCAG
additive_decomposition3 = seasonal_decompose(df2['Mean'], model='additive', period=12) 

plt.rcParams.update({'figure.figsize': (16,12)})


additive_decomposition3.plot().suptitle('Tendencia, Estacionalidad y Errores', fontsize=10)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# plt.show()

from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

residuos1= additive_decomposition1.resid
residuos2= additive_decomposition2.resid
residuos3= additive_decomposition3.resid

# Graficas
fig, axes = plt.subplots(1,2,figsize=(16,3), dpi= 100)
plot_acf(residuos1.dropna(), lags=50, ax=axes[0])
plt.xlabel("Lag")
plot_pacf(residuos1.dropna(), lags=50, ax=axes[1])
plt.xlabel("Lag")
plt.show()


# Graficas
fig, axes = plt.subplots(1,2,figsize=(16,3), dpi= 100)
plot_acf(residuos2.dropna(), lags=50, ax=axes[0])
plt.xlabel("Lag")
plot_pacf(residuos2.dropna(), lags=50, ax=axes[1])
plt.xlabel("Lag")
plt.show()


# Graficas
fig, axes = plt.subplots(1,2,figsize=(16,3), dpi= 100)
plot_acf(residuos3.dropna(), lags=50, ax=axes[0])
plt.xlabel("Lag")
plot_pacf(residuos3.dropna(), lags=50, ax=axes[1])
plt.xlabel("Lag")
plt.show()
