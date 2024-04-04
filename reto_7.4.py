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