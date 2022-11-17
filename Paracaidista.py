"""
Autor: Martín R. 
Fechas: 20 de Septiembre, 2022
DESCRIPCION:
Este programa encuentra la raíz de una función no-lineal usando el método de bisección o de bolzano.

-->EJERCICIO
 La solución de la ecuación de caída libre de un paracaidista considerando la fuerza de rozamiento con el aire proporcional a su velocidad es no-lineal.

Si queremos saber por ejemplo  la razón τ = m/c para la cual la velocidad es de 20 m/s a los 5 segundos de tiempo de caída debemos hacer el cálculo de forma númerica.
"""


import numpy as np

def f(tau):
	v=20
	g=9.8
	t=5
	ftau=v/g-tau*(1-np.exp(-t/tau))
	return (ftau)

tau=0.5
lista=[]
step = 0.5	
for i in np.arange(1,5,step):
	valor=f(i)
	lista.append(valor)
	tau=tau+step
	if f(i)*f(i-1)>0:
		print(f"tau={tau} | f({tau}): {valor:.5f} ")
	else:
		print(f"tau={tau} | f({tau}): {valor:.5f} ")
		break 

xl=tau-step
xu=tau
print(f"Notamos que la función cambia de signo entre tau={xl} y tau={xu} \n entonces escogemos ->xl={xl} ,xu={xu} para comenzar el método de bisección ")

counter=1
xr_a=0
error=1
while error>0.00001:
	xr=(xu+xl)/2
	if f(xl)*f(xr)<0:
		xu=xr
		error=abs((xr-xr_a)/xr)
		print(f"{counter}.- Raiz: {xr:.5f} --> Error: {error:.5f}")
	elif f(xl)*f(xr)>0:
		xl=xr
		error=abs((xr-xr_a)/xr)
		print(f"{counter}.- Raíz: {xr:.5f} -->  Error: {error:.5f}")
	elif f(xl)*f(xr)==0:
		print(f"La raiz es: {xr:.5}  ||  No. de iteraciones: {counter}")
		break
	xr_a=xr
	counter=counter+1 
		





