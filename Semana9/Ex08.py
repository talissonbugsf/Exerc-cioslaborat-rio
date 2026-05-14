intervalo = 0
fora_intervalo = 0

for contador in range(10):
    numeros = int(input("Digite o número:"))
    
    if numeros >= 10 and numeros <= 20:
        intervalo += 1
    else:
        fora_intervalo += 1

print("Números dentro do intervalo:", intervalo)
print("Números fora do intervalo:", fora_intervalo)
