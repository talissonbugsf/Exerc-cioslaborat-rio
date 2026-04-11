contador = 1
entre_15e25 = 0

while contador <= 10:
    temperatura = float(input("Digite a temperatura da cidade:"))
    
    if temperatura >= 15 and temperatura <= 25:
        entre_15e25 += 1
    else:
        pass
    
    contador += 1

print("A quantidade de cidades que ficaram com a temperatura entre 15°C e 25°C é:", entre_15e25)
