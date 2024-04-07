# Reto_7
Por: Juan Diego Cárdenas Olarte
### Grupo: 
#### Infinity Bit Team (∞BT)

[![logo.jpg](https://i.postimg.cc/pdcVKPsT/logo.jpg)](https://postimg.cc/JyJWLCVV)

Este repositorio contiene todos los ejercicios planteados del reto 7 del curso de programación.

>### Punto 1.
>Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
i=1 #Desde este numero se inicia
while (i<=100): #Define las condiciones del bucle (hasta que i=100)
    print(i**2) # imprime en consola i al cuadrado
    i+=1 # Adiciona uno a i cada que se inicia el bucle
```
#### Diagrama de flujo:
```mermaid
flowchart TD
    A(Inicio) --> B[i=1]
    B -->F{Si i <= 100}
    F -->|si| G[EImprimir i al cuadrado]
    F --> |no|L(Fin)
    G -->J[Sumar 1 a i 'i+=1' ]
    J -->F
    
```
>### Punto 2.
```python
print ("Estos son los impares: ")
i=1
e=1
while (i<=999):
    if i%2 != 0:
        print(i)
    i+=1
print ("Estos son los pares: ")
while (e<=1000):
    if e%2 == 0:
        print (e)
    e+=1
```
>### Punto 3.

```python
i=int(input("Escribe un numero entero: "))
while (i>=2):
    if i%2 == 0:
        print (i)
    i-=1
```

>### Punto 4.

```python
i=1
e=1
pais_a: int= 25000000
pais_b: int= 19800000
while (pais_b<=pais_a):
    pais_a+=pais_a*0.02
    pais_b+=pais_b*0.03
    i+=1
año:int=i+2022
print(f"La población del pais b superara a la del pais a en el año {año}")
```

>### Punto 5.

```python
i=int(input("Escribe un numero entero: "))
factorial:int=1
while (i>=2):
    factorial*=i
    i-=1
print(factorial)

```

>### Punto 6.

```python
import random
if __name__== "__main__":
    numero:int=random.randint(1,100)
    intento=int(input("Intenta adivinar un numero entre 1 y 100: "))
    while intento!=numero:
    
        if intento>numero:
            print("El numero buscado es menor")
        else:
            print("El numero buscado es mayor")
        intento=int(input("Intenta de nuevo: "))
    print("El numero es correcto")
```

>### Punto 7.

```python
import random
numero:int= random.randint(2,50)
guardar=numero
while (guardar>0):
    if numero%guardar == 0:
        print(guardar)
    guardar-=1
```

>### Punto 8.

```python

```
