'''
Título: Implemetación del filtro de Kalman en python.

Descripción: 
-Primero crea una señal a partir de un proceso aleatorio de tipo gauss-markov  y la graficamos

-Posterior a esto generamos una señal, a partir de la primera, con ruido blanco y hacemos una gráfica de ambas señales para comparar.

-Por último implementamos el algoritmo de filtro de kalman para generar una señal filtrada a partir de la señal con ruido y comparamos el MSE(error cuadrático medio) con la señal original.

Autor: Martín R.
Fecha: Noviembre 21

'''
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Generar una realización del proceso aleatorio
#Modelo de Gauss-Markov

N=30 #tamaño de la señal
a=0.5 #valor de la constante del proceso

sigma_u=1 #varianza del proceso

#Inicializar la señal
s=np.zeros(N)
for n in np.arange(1,N):
	s[n]=a*s[n-1]+np.random.randn(1)*sigma_u #Señal
	 #Ruido gaussiono/blanco

plt.plot(s,label='realización del proceso aleatorio')
plt.legend()
plt.show()

#Generar la señal con ruido a partir de la realización
sigma_n = 1.2 #Varianza del ruido
sr=np.zeros(N) #Señal con ruido
#Agregar ruido
for n in np.arange(1,N):
	sr[n]=s[n]+np.random.randn(1)*sigma_n


#Segundo esto
#Calcular el MSE entre las señales
errorR=((sr-s)**2).mean()
plt.plot(s,'--',label='realización del proceso aleatorio')	
plt.plot(sr,label='señal con ruido con un error de: '+str(errorR))
plt.legend()
plt.show()

#construir el filtro de kalman

s_pred=0 #prediccion anterior empieza en cero
M=0
s_hat=np.zeros(N)

for n in np.arange(N):
	#Predicción
	s_pred=a*s_pred
	error=sr[n]-s_pred
	#Calcular prediccion de mínimo MSE
	M=a**2*M+sigma_u
	#Calcular la ganancia de kalman
	K=M/(sigma_n+M)
	#Calcular el estimador en base a la corrección de la predicción 
	s_pred=s_pred+K*error
	s_hat[n]=s_pred # guardar señal fitrada para graficar
	#actualizar la predicción del Mínimo MSE
	M=(1-K)*M


#Calcular el MSE de la estimación
errorK=((s_hat-s)**2).mean()

plt.plot(s,'--',label='realización del proceso aleatorio')	
plt.plot(sr,label='señal con ruido con un error de: '+str(errorR))
plt.plot(s_hat,label='Estimación kalman con un error de: '+str(errorK))
plt.legend()
plt.show()
	

#Después de lo de arriba; intesificar el ruido con la variaza sigma_n=1.2
	
	
	
	
	
	
	
	
	
	
	
	
