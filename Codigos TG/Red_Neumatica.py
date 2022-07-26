# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 21:30:46 2021

@author: CAMILO VELARTT
"""

#Librerias necesarias
import math
from math import pi

#Calcular el diametro


Q=float(input("Rango de Flujo de Aire (Real) [m³/min] "))
v=float(input("Ingrese velocidad u [m/s]: "))

D = math.sqrt((4*Q)/((pi)*v*60))

Diametro = D

print("")
print("El diametro es, en (m)")
print(D)
print("")

print("")
print("Ahora se calcula Reynolds")

#Variables del fluido - TABLAS
print("Dene ingresar la Temperatura de Trabajo: ")
ff = (input("Revise la tabla y obtenga (Densidad) y (Viscosidad dinamica): "))


import os
os.popen('TABLA00.pdf')

Rho=float(input("Ingrese Densidad Rho [kg/m3]: "))
Nu=float(input("Ingrese Viscosidad cinematica Mu [cPa]: "))
Mu = Nu/Rho
Visc_cin = Mu

#Calcular regimen de flujo - No de Reynolds

Re = (1000*v*D)/Mu
Reynolds = Re
print("")
print("El número de Reynolds es: ")
print(Re)
print("")
if Re > 4000:
    print("Re > 4000 ")
    print("Se encuentra en régimen de flujo TURBULENTO")
elif 2300 < Re <=4000:
    print("Se encuentra el FLUJO EN DESARROLLO")

else:
    print("Re < 2300 Se encuentra en régimen de flujo LAMINAR")

#Calcular el factor de fricción
import os
os.popen('cfr.pdf')


def f(x):
    return 1/x**0.5+2*math.log10((e/D)/3.7+2.51/(Re*x**0.5))

e=float(input("Ingrese Rugosidad e [m]: "))

import os
os.popen('Accesorios.pdf')

def Df(x):
    return -0.5*x**-1.5+2*(-2.51*x**-1.5/(2*Re))*math.log10(2.7182)/((e/D)/3.7+2.51/(Re*x*0.5))
x0=0.015
i=1
for iteracion in range (1,11):
    x1= x0-f(x0)/Df(x0)
    x0=x1
    print("iteracion", i,x0)
    i=i+1
print("")
print("El factor de fricción f es:")
print(x0)
print("")
#Cálculo de los coeficientes de resistencia
#locales (Ki) en codos, tee y válvulas
f=int(input("Cantidad total de accesorios presente "))
tp=f
def fun(k_1):
        return (k_1)
li=[]
for x in range (f):

    k_1=float(input("Ingrese Rugosidad K : "))
    print(fun(k_1))

    fun(k_1)
    li.append(fun(k_1))
print("")
print(li)
rt = sum(li)
print("")
print("La perdida total por accesorios es")
print(rt)

#CAIDA DE PRESIÓN
L=float(input("Ingrese Longitud [m]: "))
v_esp=1/Rho
hf = (((x0*(L/D)+(rt/10))*(v**2/2*v_esp))/10000)
print("")
print("La perdida total en la tuberia es [bar]: ")
print(hf)
#FIN