# -*- coding: utf-8 -*-
"""
Created on Sun Apr2021

@author: CAMILO VELARTT
"""

#Cálculo de la temperatura de proyecto

def Temp_Proyc(Tmax,Tmed ):
    return 0.4*Tmax + 0.6*Tmed

Tmax=float(input("Ingrese Tmax del lugar [°C]: "))
Tmed=float(input("Ingrese Tprom del luhgar [°C] : "))

t1 = Tmax
t2 = Tmed

print("")
print("La temperatura del proyecto T ext prom sera [K]: ")
print(Temp_Proyc(Tmax,Tmed) + 273.15)

#Coeficiente global de perdidas

def Coef_Glo(h_i, h_e, esp, resis, ):
    return 1/((1/h_i)+(esp/resis)+(1/h_e))

h_e=float(input("Ingrese coeficiente de conveción de la superficie interior [W/m2*K]: "))
h_i=float(input("Ingrese coeficiente de conveción de la superficie exterior [W/m2*K]: "))
esp=float(input("Ingrese espesor de ailamiento: "))
resis=float(input("Ingrese resitencia de la materia [W/m*K]: "))

print("")
print("El coeficiente del global de perdidas U [W/m2*K]: ")
print(Coef_Glo(h_i, h_e, esp, resis))


#Calculo de flujo de calor a través de las paredes
def Transf_calor(U, A, T_ext, T_int):
    return U*A*((T_ext)-(T_int))


T_ext=float(input("Ingrese T ext prom [K] "))
T_int=float(input("Ingrese T int [K] "))
print("")
print("")
print("Ahora se calcula el calor transferido Q es [W] ")

lie = []

for x in range(6):
    
    U=float(input("Ingrese Coeficiente global de perdidas[W/m2*K]: "))
    base=float(input("Ingrese base pared [m] "))
    altura=float(input("Ingrese altura pared [m] "))
    A = base*altura 
    print("")
    print("Calor transferido [W] ")
    print(Transf_calor(U, A, T_ext, T_int))
    
    Transf_calor(U, A, T_ext, T_int)
    lie.append(Transf_calor(U, A, T_ext, T_int))

print("")
print(lie)
   
cal_2 = sum(lie)
cal_2=cal_2/0.86

print("")
print("El calor total transferido por las paredes del cuarto [W]")
print(cal_2)


# Calculo del calor transferido del producto

def Calor_pro(m_pro, c, T_ent, T_fin, hrs):
    return m_pro*c*(T_ent - T_fin)/hrs

m_pro=float(input("Ingrese masa de producto [kg]: "))
c=float(input("Ingrese calor especifico [kcal/kg*°C]: "))
T_ent=float(input("Ingrese T a la que entra el producto: °[C] "))
T_fin=float(input("Ingrese T esperada en la camara: °[C] "))
hrs=int(input("Ingrese tiempo de operación [hrs]: "))

cal_3 = Calor_pro(m_pro, c, T_ent, T_fin, hrs)
cal_3=cal_3/0.86


print("")
print("El calor transferido del producto: [W] ")
print(cal_3)

#Calculo apertura puerta - filtraciones de aire

def Calor_filtr(Vol_cam, NRH, dens_aire, cp, T_ent_aire, T_fin_aire):
    return Vol_cam*NRH*dens_aire*cp*(T_ent_aire-T_fin_aire)

Vol_cam=float(input("Ingrese volumen de la camara [m3]: "))
NRH=float(input("Ingrese número de renovaciones hora del aire de la cámara.: "))
dens_aire=float(input("Ingrese densidad del aire estándar "))
cp=float(input("Ingrese calor específico del aire: °[kcal/kg °C] "))
T_ent_aire=float(input("Ingrese T a la que entra el aire: °[C] "))
T_fin_aire=float(input("Ingrese T esperada en la camara: °[C] "))

cal_4 =Calor_filtr(Vol_cam, NRH, dens_aire, cp, T_ent_aire, T_fin_aire)
cal_4 = cal_4/0.86

print("")
print("El calor producido por las fluctuaciones de aire [kcal/h]: ")
print(cal_4)
    

# Calcular calor generado por las iluminación

def Cal_ilum(P, n):
    return P*n

P=float(input("Ingrese potencia luminaria [W]: "))
n=float(input("Ingrese numero de luminarias: "))

cal_5 = Cal_ilum(P, n)

print("")
print("El calor producido por la iluminación es [kcal/h]: ")
print(cal_5)

#Ganancia de calor originada por trabajadores

def Cal_pers(q,num, time):
    return (q*num*time)

q=float(input("Ingrese calor por persona en (W) : "))
num=float(input("Ingresenúmero de personas en la cámara : "))
time=float(input("Ingrese tiempo de permanencia en horas/día: "))

cal_6 = Cal_pers(q, num, time)
cal_6 = cal_6/0.86

print("")
print("El calor liberado por las personas es [W] ")
print(cal_6)

#Carga térmica total de la camara

Q_T = cal_2 + cal_3 + cal_4 + cal_5 + cal_6

print("")
print("La carga térmica total es [W]: ")
print(Q_T)





