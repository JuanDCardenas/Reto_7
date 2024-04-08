def numeros_primos (numero:int)->bool: 
    j=2
    if numero==1 :
        return False
    if numero==2 :
        return True
    while (j<numero):
        if numero%j==0:
            return False
        j+=1
    return True    
        
if __name__ == "__main__":
    numero:int=1
    while (numero<=100):
        primo=numeros_primos(numero)
        if primo==True:
            print(numero)
        numero+=1
