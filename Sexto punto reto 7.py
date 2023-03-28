# 6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.

import random
r =numero_a_adivinar = random.randint(1, 100)

print("Adivina un numero entre el 1 a 100")

while True:
    respuesta = input("¿Es el número " + str(numero_a_adivinar) + "? (mayor/menor/igual): ")
    
    if respuesta == "mayor":
        numero_a_adivinar = random.randint(numero_a_adivinar+1, 100) # El número a adivinar es mayor
    elif respuesta == "menor":
        numero_a_adivinar = random.randint(1, numero_a_adivinar-1) # El número a adivinar es menor
    elif respuesta == "igual":
        print("¡Ganaste! el numero es "+ str(numero_a_adivinar))
        break # Salir del bucle mientras
    else:
        print("Respuesta inválida. Por favor, ingrese 'mayor', 'menor' o 'igual'")