# Primer punto 

Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

## Diagrama de flujo 
![Primer punto reto 7](https://user-images.githubusercontent.com/124607325/228106161-4fb4d7ed-14bd-465f-a73e-000f25f6636a.png)



     # Inicializa una variable 'i' con el valor 1
     i = 1

     # Mientras 'i' sea menor o igual a 100, ejecuta el siguiente bloque de código
     while i <= 100:
     # Imprime el valor actual de 'i' y su cuadrado
     print(i, i**2)
     # Incrementa el valor de 'i' en 1 para la siguiente iteración
    i  += 1
    
    
    
 Para hacer este programa se realiza: 


![Primer punto reto 7](https://user-images.githubusercontent.com/124607325/228106277-e1b1164e-9e4f-42d1-8078-debc50c6eccd.png)


1. se le da un valor inicial a 'i' con el valor 1.

2. Luego, el bucle while se ejecuta siempre que el valor de 'i' sea menor o igual a 100.

3. Dentro del bucle, se imprimen los valores de 'i' y 'i' al cuadrado utilizando la función 'print'.

4. Luego, se incrementa el valor de 'i' en 1 con la expresión 'i += 1'.

Este proceso continúa hasta que el valor de 'i' sea mayor que 100 y, en ese punto, el bucle se detendrá y el programa terminará.

Nos imprime una lista asi: 



![Primer punto lista 1](https://user-images.githubusercontent.com/124607325/228106317-3cae5192-375e-466e-b38b-d1a8bcf989f4.png)



# Segundo Punto

Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

## Diagrama de flujo 

![Segundo punto reto 7](https://user-images.githubusercontent.com/124607325/228106555-bd67fe88-3593-4f79-8cc0-ed06f0fbc218.png)



    # Inicializa dos variables 'i' y 'j' con los valores 1 y 2, respectivamente
     i = 1 
     j = 2 

    # Mientras 'i' sea menor o igual a 999 y 'j' sea menor o igual a 1000, ejecuta el siguiente bloque de código
    while i <= 999 and j<=1000: 
    # Imprime los valores actuales de 'i' y 'j', separados por una coma y un espacio
     print(i, j, sep = ", ")
    # Incrementa el valor de 'i' y 'j' en 2 para la siguiente iteración
    i += 2


Para hacer este programa se debe: 

![Segundo punto reto ](https://user-images.githubusercontent.com/124607325/228107791-d4e47f6f-e7cf-4954-a902-74407045654a.png)

1. Se les asigna el valor a las variables i y j, se inician las variables i y j en 1 y 2.

2. Se establece una condición en el while: mientras i sea menor o igual a 999 y j sea menor o igual a 1000, se ejecutará el bucle.

3. Se imprime el par ordenado actual, utilizando la función print. 

4. Se actualiza el valor de i agregando 2 unidades, y lo mismo para j.

5. El bucle se repite desde el paso 2 mientras se cumpla la condición.

6. Cuando se alcanza la condición de salida del bucle, la ejecución del programa finaliza.

Se imprime una lista asi: 


![Segundo punto lista](https://user-images.githubusercontent.com/124607325/228108231-fa49822d-42ac-4dce-aa63-2543bf124e28.png)



# Tercer Punto

Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

##  Diagrama de flujo 
![Tercer punto reto 7](https://user-images.githubusercontent.com/124607325/228108626-cfd29180-2719-4fb7-bea9-ada5aa445669.png)



     # Solicita al usuario que ingrese un número y lo convierte a un entero utilizando la función 'int'
     n= int(input("Ingrese un número natural mayor o igual a 2: "))

     # Si el número ingresado es mayor o igual a 2, ejecuta el siguiente bloque de código
     if n >= 2:
       # Establece el valor de la variable 'i' como 'n' si 'n' es par, o como 'n-1' si 'n' es impar
       i = n if n % 2 == 0 else n - 1  
       # Mientras 'i' sea mayor o igual a 2, ejecuta el siguiente bloque de código
         while i >= 2:
        # Imprime el valor actual de 'i'
        print(i)
        # Resta 2 al valor de 'i' para la siguiente iteración
        i -= 2
# Si el número ingresado es menor que 2, imprime el mensaje "El número ingresado es menor que 2."
else:
    print("El número ingresado es menor que 2.")


Para hacer este programa se debe: 

![Tercer punto reto 7](https://user-images.githubusercontent.com/124607325/228108676-d0b70667-c2b9-4f07-bca3-00640ef8563f.png)


1. Se solicita al usuario que ingrese un número natural mayor o igual a 2.

2. Se establece que si el número ingresado es mayor o igual a 2, se ejecutará el programa. De lo contrario, se imprimirá "El número ingresado es menor que " y el programa terminará.

3. Se establece la variable i igual al número ingresado si es par, y si es impar se establece como el número ingresado menos 1. Esto asegura que i sea un número par.

4. Se establece un bucle while: mientras i sea mayor o igual a 2, se ejecutará el bucle.

5. Se imprime el valor de i utilizando la función print.

6. Se actualiza el valor de i restando 2 unidades.

7. El bucle se repite desde el paso 4 mientras se cumpla la condición.

8. Cuando se alcanza la condición de salida del bucle, el programa termina.

Se imprime una lista  asi: 


![Tercer punto lista](https://user-images.githubusercontent.com/124607325/228110151-de030b31-fdb3-4f07-b577-8929b1fb584b.png)


# Cuarto Punto 

En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18:9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.


     # Establece las poblaciones iniciales de los países A y B en millones
     PoblacionA = 25
     PoblacionB = 18.9

      # Establece las tasas de interés anuales de los países A y B
      Tasa_paisA = 0.02
      Tasa_paisB = 0.03

      # Solicita al usuario que ingrese el año de inicio para el cálculo
      n= int(input("Ingrese el año en el que quiere comenzar: "))
      Año_actual= n

     # Mientras la población del país B sea menor o igual que la del país A, ejecuta el siguiente bloque de código
      while PoblacionB <= PoblacionA:
    
          # Calcula la nueva población del país A después de un año utilizando su tasa de interés
            PoblacionA *= (1 + Tasa_paisA)
          # Calcula la nueva población del país B después de un año utilizando su tasa de interés
            PoblacionB *= (1 + Tasa_paisB)

       # Incrementa el año actual en 1 para la siguiente iteración
         Año_actual += 1
    
        # Imprime el año en el que la población del país B superará a la del país A
        print("La población del país B superará a la del país A en el año "+str(Año_actual))

Para realizar este programa se hace: 

![Cuarto Punto reto 7 1](https://user-images.githubusercontent.com/124607325/228111894-c703cce9-fb47-48d5-8835-cb14fc5a497e.png)

1. Se establecen las poblaciones iniciales de los países A y B en millones utilizando las variables PoblacionA y PoblacionB.

2. Se establecen las tasas de interés de los países A y B utilizando las variables Tasa_paisA y Tasa_paisB.

3. Se solicita al usuario que ingrese el año en el que desea comenzar el cálculo , se establece la variable Año_actual igual al año ingresado por el usuario.


![Cuarto Punto reto 7 2](https://user-images.githubusercontent.com/124607325/228112037-6595b060-83ed-46a5-b72e-8207b666505d.png)

4. Se establece un bucle while: mientras la población del país B sea menor o igual a la población del país A, se ejecutará el bucle.

5. Se actualiza la población de los países A y B utilizando la fórmula de crecimiento exponencial: Poblacion *= (1 + Tasa_pais).

6. Se actualiza la variable Año_actual sumando 1.

7. El bucle se repite desde el paso 5 mientras se cumpla la condición.

8. Cuando se alcanza la condición de salida del bucle, se imprime un mensaje indicando el año en el que la población del país B superará a la población del país A utilizando la función print. en este caso se usa el 2023 para dar el ejemplo de respuesta: 

 ![Cuarto Punto respuesta 2023](https://user-images.githubusercontent.com/124607325/228112418-3b6378e9-18a5-4eaf-9d40-b86addd468d4.png)
 
 
 # Quinto Punto 
 
 Imprimir el factorial de un número natural n dado.
 
 
     # Solicita al usuario que ingrese un número natural
     n = int(input("Ingrese un número natural: "))

      # Definición de la función para calcular el factorial
       def factorial(n):
         resultado = 1 # Inicializa el resultado en 1
          i = 1 # Inicializa el contador en 1
         terminado = False # Establece una bandera para controlar el ciclo
        while not terminado: # Mientras la bandera no sea verdadera
           resultado *= i # Multiplica el resultado por el valor del contador
              i += 1 # Incrementa el contador en 1
              if i > n: # Si el contador supera el valor de n
             terminado = True # Establece la bandera en verdadero para salir del ciclo
          return resultado # Retorna el resultado del factorial

     # Imprime el resultado del factorial del número ingresado por el usuario
      print("El factorial de " + str(n) + " es " + str(factorial(n)))

 
 Para realizar este programa se hace: 
 ![Quinto punto reto 7](https://user-images.githubusercontent.com/124607325/228114015-a4b88f00-ab0c-4bde-b2fa-22cd5fc7c6db.png)

 1. Se  solicita igresar número natural, que se almacena en la variable "n".
 
 2. Se define la función factorial(n), que toma un argumento "n" y devuelve el factorial de ese número.
 
 3. Se inician las variables "resultado" e "i" en 1, que se utilizarán para almacenar el resultado del cálculo del factorial y para realizar el bucle while.
 
 4. Se establece la variable "terminado" como False, lo que indica que el bucle while se ejecutará al menos una vez.

5. Se inicia un bucle while que se ejecutará mientras "terminado" sea False. En cada iteración, el valor de "resultado" se multiplica por "i" y "i" se incrementa en 1.

6. Se verifica si "i" es mayor que "n". Si es así, se establece "terminado" como True y el bucle while se detiene.

7. La función devuelve el valor de "resultado".

Y se  imprime un mensaje que indica el factorial del número ingresado: En este caso se hace el ejemplo con el factorial de 20.
![Quinto punto resultado](https://user-images.githubusercontent.com/124607325/228114396-0086b8b4-a8b5-48cd-bf4b-9d94f6914fb2.png)


# Sexto Punto 

Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.


     # Importa la librería 'random'
     import random

     # Genera un número aleatorio entre 1 y 100
     numero_a_adivinar = random.randint(1, 100)

     # Muestra el mensaje al usuario
     print("Adivina un número entre el 1 a 100")
 
     # Inicia un bucle que se ejecuta hasta que el usuario adivina el número
     while True:
       # Solicita al usuario que indique si el número a adivinar es mayor, menor o igual
        respuesta = input("¿Es el número " + str(numero_a_adivinar) + "? (mayor/menor/igual): ")
    
       # Si el usuario indica que el número a adivinar es mayor
       if respuesta == "mayor":
         numero_a_adivinar = random.randint(numero_a_adivinar+1, 100) # Genera un número aleatorio mayor al anterior
       # Si el usuario indica que el número a adivinar es menor
         elif respuesta == "menor":
         numero_a_adivinar = random.randint(1, numero_a_adivinar-1) # Genera un número aleatorio menor al anterior
       # Si el usuario adivina el número
         elif respuesta == "igual":
        print("¡Ganaste! el número es " + str(numero_a_adivinar)) # Muestra el mensaje de felicitación
        break # Sale del bucle 'while'
       # Si la respuesta no es válida
         else:
        print("Respuesta inválida. Por favor, ingrese 'mayor', 'menor' o 'igual'")


 Para realizar este programa se hace: 
 
![Sexto punto reto 7](https://user-images.githubusercontent.com/124607325/228116038-920e9613-8f3c-4bca-a8cd-61eaf321b634.png)

1. Se importa el módulo "random" de Python para generar números aleatorios.

2. Se usa la  función "randint()" del módulo "random" para generar un número aleatorio entre 1 y 100. Este número es el que el jugador tendrá que adivinar.

3. El programa imprime en pantalla el mensaje "Adivina un número entre el 1 a 100".


![Sexto punto reto 7 1](https://user-images.githubusercontent.com/124607325/228116026-1fb719fe-a208-4d44-9495-f6c4cdd0e21a.png)

4. A continuación, comienza un bucle "while True" que se ejecutará hasta que el jugador adivine el número.

5. En cada iteración del bucle, el programa le pide al jugador que ingrese si el número a adivinar es mayor, menor o igual al número que sugiere el programa.


![Sexto punto reto 7 preguntas ](https://user-images.githubusercontent.com/124607325/228116031-eca6523a-5189-4e6d-9caa-136e2078da75.png)

Si se ingresa "mayor", el programa genera un nuevo número aleatorio entre el número que sugiere el programa + 1 y 100 
Si se ingresa "menor", el programa genera un nuevo número aleatorio entre 1 y el número que sugiere el programa - 1 
Si se ingresa "igual", el programa imprime en pantalla el mensaje "¡Ganaste!" junto con el número que había elegido el programa. Luego, el programa sale del bucle.

6. Si se ingresa cualquier otra cosa, el programa imprime en pantalla el mensaje "Respuesta inválida. Por favor, ingrese 'mayor', 'menor' o 'igual'" y comienza una nueva iteración del bucle.

7. si se adivina el número, el programa imprime en pantalla el mensaje "¡Ganaste!" junto con el número que había elegido el programa y sale del bucle.

![Sexto punto reto respuesta](https://user-images.githubusercontent.com/124607325/228116050-99fbee24-8367-4e86-9fdd-74aa66718b57.png)


# Septimo Punto 

Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.



     # Solicita al usuario que ingrese un número del 2 al 50
     n = int(input("Ingrese un número del 2 al 50: "))

     # Inicializa el contador en 2
     i = 2

      # Imprime el mensaje para informar al usuario sobre los divisores del número ingresado
      print("Los divisores de", n, "son:")

      # Mientras el número ingresado esté dentro del rango del 2 al 50
         while 2 <= n <= 50:
       # Si el número es divisible por el valor actual del contador
         if n % i == 0:
       # Imprime el valor del contador, que es un divisor del número ingresado
         print(i)
    
       # Incrementa el valor del contador en 1
       i += 1

 Para realizar este programa se hace:
 
 ![Septimo punto reto 7 ](https://user-images.githubusercontent.com/124607325/228117275-bccd58eb-a4db-4b21-9573-7d7540eec709.png)
 
1. Se pide ingresar un numero entre 2 y 50, y se almacena en la variable n.

2. Se inicia otra variable llamda i, que se inicia en 2 que es el primer posible divisor 

3. Se inicia el ciclo while  en que si 2 es  <= n y n es <= 50, esto para que n este en ese rango Si el número n es menor que 2 o mayor que 50, el ciclo no se ejecutará.

4, Se inicia una condición if n % i == 0:  la cual comprobara si el número n es divisible por el número i. Si es así, el número i es un divisor de n y se imprimirá.

5. Para seguir con el bucle se aumenta el valor de i en 1 para que el siguiente número se compruebe.

Cuando se han comprobadoel ciclo termina y el programa finaliza.

En este caso para comprobar se prueba con el numero 35.

![Septimo punto respuesta](https://user-images.githubusercontent.com/124607325/228117273-4121b324-71c5-421c-9021-fa1e28ac1eb4.png)


# Octavo Punto 

Implementar el algoritmo que muestre los números primos del 1 al 100. nota: use funciones

     # Define la función 'es_primo' que recibe un número entero como argumento y devuelve 'True' si el número es primo o 'False' en caso contrario
     def es_primo(numero: int) -> bool:
     # Si el número es menor que 2, devuelve 'False'
     if numero < 2:
     return False
     i = 2
     # Mientras 'i' sea menor que el número, ejecuta el siguiente bloque de código
      while i < numero:
     # Si el número es divisible entre 'i', devuelve 'False'
     if numero % i == 0:
     return False
      i += 1
    # Si no se ha encontrado un divisor entre 2 y el número-1, devuelve 'True'
     return True

     # Define la función 'Lista_numeros_primos' que recibe un número entero como argumento y devuelve una lista con los números primos mayores o iguales que el argumento y menores o iguales que 100
      def Lista_numeros_primos(n: int) -> list[int]:
      numeros_primos = []
       # Mientras el número 'n' sea menor o igual que 100, ejecuta el siguiente bloque de código
      while n <= 100:
       # Si 'n' es un número primo, agrega 'n' a la lista 'numeros_primos'
         if es_primo(n):
       numeros_primos.append(n)
       n += 1
      # Devuelve la lista de números primos
       return numeros_primos
      # Establece el valor inicial de 'numero' en 1
      numero = 1

      # Mientras 'numero' sea menor o igual que 100, ejecuta el siguiente bloque de código
      while numero <= 100:
      # Si 'numero' es un número primo, lo imprime
       if es_primo(numero):
       print(numero)
     # Incrementa el valor de 'numero' en 1 para la siguiente iteración
      numero += 1

 Para realizar este programa se hace:

![Octavo punto reto 7 1](https://user-images.githubusercontent.com/124607325/228119283-6283641c-16a1-435a-a7f8-ff75d1d2be12.png)

1. Se declara La función es_primo que comprueba si un número es primo. Si el número es menor que 2, devuelve False. Si el número es divisible por cualquier número entre 2 y el número menos uno devuelve False. Si el número no es divisible por ningún número entre 2 y el número menos 1 devuelve True.

![Octavo punto reto 7 2](https://user-images.githubusercontent.com/124607325/228119284-81c30713-0b46-4c65-ac12-81a213952728.png)


2. Se declara la función Lista_numeros_primos que crea una lista vacía llamada numeros_primos y encuentra todos los números primos desde n hasta 100 utilizando el ciclo while. Si el número es primo, se agrega a la lista de numeros_primos. Después de encontrar todos los números primos, se devuelve la lista de numeros_primos.

3.  Se define un ciclo while donde se  asegura de que los números del 1 al 100 sean comprobados para ser primos. Si el número es primo, se imprime utilizando la función es_primo(numero).

![Octavo punto reto 7 3](https://user-images.githubusercontent.com/124607325/228119285-ec00330e-4d46-4677-9643-c99a07277369.png)

4. en if es_primo se comprueba si el número numero es primo utilizando la función es_primo(numero). Si es primo, se imprime utilizando la función print(numero).

5. Y se aumenta el valor de numero en 1 para que el siguiente número se compruebe en la siguiente iteración.

6. Cuando se han comprobado todos los números del 1 al 100, el ciclo termina y el programa finaliza.

La lista que se imprime es asi: 

![Octavo punto reto 7  respuesta](https://user-images.githubusercontent.com/124607325/228119282-f49d9e12-bd19-406e-8247-845cc71d48f1.png)
