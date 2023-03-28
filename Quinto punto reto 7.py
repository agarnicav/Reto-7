# 5. Imprimir el factorial de un número natural n dado.

n = int(input("Ingrese un número natural: "))

def factorial(n):
    resultado = 1
    i = 1
    terminado = False
    while not terminado:
        resultado *= i
        i += 1
        if i > n:
            terminado = True
    return resultado

print(factorial(n))