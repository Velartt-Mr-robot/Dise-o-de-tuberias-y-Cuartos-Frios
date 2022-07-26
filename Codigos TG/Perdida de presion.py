5# -*- coding: utf-8 -*-
"""
Created on April 2021
@author: CAMILO VELARTT
"""

#INICIO
import matplotlib.pyplot as plt
from skimage import io
import math
from math import pi

print("")
print ("Ingrese unicamente [si] o [no]")
opcion1 = input ('Se utilizará una presión < 100 bares: ')
print("")

#Tipo de Caldera

if opcion1 == 'si':
     print ('Se recomienda usar una CALDERA PIROTUBULAR')
   
elif opcion1 == "no":
    print ('Se recomienda usar una caldera acuotubular')

    temp = input ('Ingrese temperatura mas alta requerida:')
    presion = input ('Ingrese presion mas alta requerida:')
 
else:
     print ("Ingrese unicamente [si] o [no]")
     opcion1 = input ('Se utilizará una presión < 100 bares: ')

#Rango de caldera
print("")
print ("Ingrese la presión máxima requerida")
print ("Ingrese el flujo másico de vapor máximo requerido")

P_max = float(input("Ingrese presión máxima requerida [bar]: "))

if P_max == 10:
    print("T_sat = 179.9 [°C]")
elif P_max == 9:
    print("T_sat = 175.4 [°C]")
elif P_max == 8:
    print("T_sat = 170.4 [°C]")
elif P_max == 7:
    print("T_sat = 165.0 [°C]")
elif P_max == 6:
    print("T_sat = 158.9 [°C]")
elif P_max == 5:
    print("T_sat = 151.9 [°C]")
elif P_max == 4:
    print("T_sat = 143.6 [°C]")
elif P_max == 3:
    print("T_sat = 133.6 [°C]")
elif P_max == 2:
    print("T_sat = 120..2 [°C]")
elif P_max == 1:
    print("T_sat = 99.9 [°C]")
else:
    print("Escoja un valor de (1,10) bares")
    P_max = float(input("Ingrese presión máxima requerida [bar]: "))

#Calcular BHP, según la ASME 1 BHP=15.65 [kg/h]

mv_max =  float(input("Ingrese flujo másico de vapor máximo requerido [kg/h]: "))

BHP = (mv_max/15.65)
Potencia = BHP

print("")
print("Potencia requerida " + str(BHP) + " BHP")


#Calcular caudal que recorrera la tuberia principal
ff = (input("revise la tabla y obtenga su valor en: [m3/kg] "))

image=io.imread("tablas_termo.png")/255.0 # imread lee las imagenes con los pixeles codificados como enteros 
# en el rango 0-255. Por eso la convertimos a flotante y en el rango 0-1

plt.imshow(image,vmin=0,vmax=5)
plt.show()

import os
os.popen('Tablas Termo.pdf')



v_esp =  float(input("Ingrese volumen especifico a la presión especificada: [m3/kg] "))

mv_max = mv_max/3.6
Q=mv_max*v_esp*10**-3
Caudal = Q

print("")
print("Caudal requerido " + str(Q) + " [m3/s]")

#Calcular el diametro

Q=float(input("Ingrese Caudal Q [m3/s]: "))
v=float(input("Ingrese velocidad u [m/s]: "))

D = math.sqrt((4*Q)/((pi)*v))

Diametro = D

print("")
print("El diametro es, en (m)")
print(D)
print("")

print("")
print("Ahora se calcula Reynolds")

#Variables del fluido - TABLAS
ff = (input("revise la tabla y obtenga su valor en: [m3/kg] "))


import os
os.popen('t2.pdf')

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

def fun(k_1, k_2):
        return (k_1/Re) + k_2*(1 + (0.0254/D))

li=[]
    
for x in range (f):
    
    k_1=float(input("Ingrese Rugosidad K1 : "))
    k_2=float(input("Ingrese Rugosidad K2 : "))
    print(fun(k_1, k_2))

    fun(k_1, k_2)
    li.append(fun(k_1, k_2))

print("")
print(li)
rt = sum(li)
print("")
print("La perdida total por accesorios es")
print(rt)

#CAIDA DE PRESIÓN
L=float(input("Ingrese Longitud [m]: "))
hf = ((x0*(L/D)*(v**2/2*v_esp))/10000)/2
print("")
print("La perdida total en la tuberia es [bar]: ")
print(hf)
#FIN