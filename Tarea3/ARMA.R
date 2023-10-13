# EJERCICIO 4 
#install.packages('TSA')
#install.packages('TSstudio') #Libreria para obtener informacion de los datos 
library('TSstudio')
library('TSA')
set.seed(910)
x <- arima.sim(n=100, model=list(ar=0.8, ma=0.4))
plot.ts(x)
acf(x)
h <- 0:20
lines(h, 0.88*(0.8)**(h-1), col="red")

eacf(x)

# Inciso c
set.seed(800)
x <- arima.sim(n=100, model=list(ar=0.8, ma=0.4))
plot.ts(x)
acf(x)
h <- 0:20
lines(h, 0.88*(0.8)**(h-1), col="red")
eacf(x)

#Inciso d

set.seed(572)
x <- arima.sim(n=48, model=list(ar=0.8, ma=0.4))
plot.ts(x)
acf(x)
h <- 0:20
lines(h, 0.88*(0.8)**(h-1), col="red")
eacf(x)

x <- arima.sim(n=200, model=list(ar=0.8, ma=0.4))
plot.ts(x)
acf(x)
h <- 0:20
lines(h, 0.88*(0.8)**(h-1), col="red")
eacf(x)





# EJERCICIO 8

data(deere3)
ts_info(deere3)
ts_plot(deere3, title = "Deere3", Xtitle = "Time", Ytitle = "Mediciones")

#acf: autocorrelation function
acf(deere3)
pacf(deere3)


final.aic <- Inf
final.order <- c(0,0,0)
for (i in 0:4) for (j in 0:4) {
  current.aic <- AIC(arima(deere3, order=c(i, 0, j)))
  if (current.aic < final.aic) {
    final.aic <- current.aic
    final.order <- c(i, 0, j)
    final.arma <- arima(deere3, order=final.order)
    }
  }
final.aic
final.order

#acf(resid(final.arma))

Box.test(resid(final.arma), lag=20, type="Ljung-Box")

eacf(deere3)

