# 8. Implementar el algoritmo que muestre los números primos del 1 al 100. nota: use funciones

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i += 1
    return True

def Lista_numeros_primos(n: int) -> list[int]:
    numeros_primos = []
    while n <= 100:
        if es_primo(n):
            numeros_primos.append(n)
        n += 1 
    return numeros_primos

numero = 1
while numero <= 100:
    if es_primo(numero):
        print(numero)
    numero += 1