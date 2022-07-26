# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:23:27 2021

@author: CAMILO VELARTT
"""


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