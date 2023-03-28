# Primer punto 

Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

## Diagrama de flujo 
![Primer punto reto 7](https://user-images.githubusercontent.com/124607325/228106161-4fb4d7ed-14bd-465f-a73e-000f25f6636a.png)
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
