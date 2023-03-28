# 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

n = int
n= int(input("Ingrese un número natural mayor o igual a 2: "))

if n >= 2:
    i = n if n % 2 == 0 else n - 1  
    while i >= 2:
        print(i)
        i -= 2
else:
    print("El número ingresado es menor que 2.")