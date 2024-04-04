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