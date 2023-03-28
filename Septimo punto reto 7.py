# 7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.

n = int(input("Ingrese un numero del 2 al 50: "))
i = 2
print("Los divisores de", n, "son:")
while 2 <= n <= 50:
    if n % i == 0:
        print(i)
    i += 1