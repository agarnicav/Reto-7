# 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

i = 1 
j = 2 
while i <= 999 and j<=1000: 
  print(i, j, sep = ", ")
  i += 2
  j += 2 

print("the end.") 