# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:14:43 2021

@author: CAMILO VELARTT
"""

#INICIO

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

v_esp =  float(input("Ingrese volumen especifico a la presión especificada: [m3/kg] "))

mv_max = mv_max/3.6
Q=mv_max*v_esp*10**-3
Caudal = Q

print("")
print("Caudal requerido " + str(Q) + " [m3/s]")






