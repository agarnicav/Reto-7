# 4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18,9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

#Pobaciones de paises A y B en Millones
PoblacionA = 25
PoblacionB = 18.9
#Tasa de interes Paises 
Tasa_paisA = 0.02
Tasa_paisB = 0.03
n = int
n= int(input("Ingrese el anio en el que quiere comenzar  "))
Año_actual= n 


while PoblacionB <= PoblacionA:
    
    PoblacionA *= (1 + Tasa_paisA)
    PoblacionB *= (1 + Tasa_paisB)

    
    Año_actual += 1
    
print("La poblacion del pais B superara a la del pais A en el año "+str(Año_actual))
