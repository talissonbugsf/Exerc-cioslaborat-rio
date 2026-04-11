contador = 1
maiores_idade = 0

while contador <= 10:
    idade = int(input("Digite a sua idade:"))
    
    if idade >= 18:
        maiores_idade += 1
    else:
        pass
    
    contador += 1
    
print("A quantidade de pessoas com mais de 18 anos de idade entrevistadas é:", maiores_idade)
