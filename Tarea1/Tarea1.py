##%%
import numpy as np 
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt  
import seaborn as sns    

##%%

# df = pd.read_csv("airlane.csv", header = None, names = ["Pasajeros"])  #Notebook
df = pd.read_csv("Tarea1/airlane.csv", header = None, names = ["Pasajeros"])
print(df)


# df.plot()

def MediaMovil(datos,q):
    '''
    Filtro de media movil uniforme.

    $\frac{1}{2q+1}\sum_{r=-q}^{q}X_{t+r}$

    Está función recibe un arreglo numpy y el parámetro q de puntos que cubre la media movil.

    Regresa un linspace apropiado para su graficación (recorrido q puntos para coincidir con los puntos que promedia) y regresa el filtrado en un arreglo tipo numpy.
    
    '''
    n = len(datos)
    T_hat = np.zeros(n-2*q)

    for i in range(n-2*q):
        aux = 0
        for j in range(2*q + 1):
            aux += datos[j + i ]

        T_hat[i] = aux/(2*q+1)
    
    x = np.linspace(q,n-2*q-1,n-2*q)  #Linspace para gráficar

    return x, T_hat

pasajeros = df['Pasajeros'].to_numpy()


q = 7    #Parámetro para número de puntos en media movil
x_hat, T_hat = MediaMovil(pasajeros,q)
x_hat_log, T_hat_log = MediaMovil(np.log(pasajeros),q)
n = len(pasajeros)


x = np.linspace(0,n-1, n)

plt.plot(x,pasajeros, label = "Serie de Tiempo de Pasajeros")
plt.xlabel("Tiempo")
plt.ylabel("Pasajeros")
plt.title("Pasajeros vs tiempo")
plt.legend()
plt.show()
plt.savefig("S1.png")


plt.plot(x, np.log(pasajeros), label = "Serie de Tiempo de Log Pasajeros")
plt.xlabel("Tiempo")
plt.ylabel("Log Pasajeros")
plt.title("Log Pasajeros vs tiempo")
plt.legend()
plt.show()
plt.savefig("S2.png")


##%%
plt.plot(x,pasajeros, label = "Serie de Tiempo de Pasajeros")
plt.plot(x_hat,T_hat, label = "Filtro de Medias Moviles")
plt.xlabel("Tiempo")
plt.ylabel("Pasajeros")
plt.title("Serie de Tiempo y su Filtración")
plt.legend()
plt.show()
# plt.savefig("MediaMovil.png")


plt.plot(x,np.log(pasajeros), label = "Serie de Tiempo de log Pasajeros")
plt.plot(x_hat_log,T_hat_log, label = "Filtro de Medias Moviles para log pasajeros")
plt.xlabel("Tiempo")
plt.ylabel("Log Pasajeros")
plt.title("Serie de Tiempo y su Filtración")
plt.legend()
plt.show()
# plt.savefig("LogMediaMovil.png")




##       BOX - PLOT
tabla = np.reshape(np.array(df), (12, 12))
tablaLog = np.reshape(np.log(np.array(df)), (12, 12))

df = pd.DataFrame(tabla.T)
df2 = pd.DataFrame(tablaLog.T)
nombres = [str(int(i)) for i in np.linspace(49, 60, 12)]
df.columns = nombres
df2.columns


df.describe()
df2.describe()


sns.boxplot(df)
plt.xlabel("Tiempo 19XX")
plt.ylabel("Pasajeros")
plt.title("Box-Plot de Pasajeros")
plt.legend()
# plt.savefig("BoxPlot1.png")

sns.boxplot(df2)
plt.xlabel("Tiempo 19XX")
plt.ylabel("Log Pasajeros")
plt.title("Box-Plot de Log Pasajeros")
plt.legend()
# plt.savefig("BoxPlot2.png")