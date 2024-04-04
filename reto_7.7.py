import random
numero:int= random.randint(2,50)
guardar=numero
while (guardar>0):
    if numero%guardar == 0:
        print(guardar)
    guardar-=1
    