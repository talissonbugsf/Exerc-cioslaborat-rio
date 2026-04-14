contador = 0
total_oliveiras = 0
maior = 0
menor = 0

while contador != 7:
    qntd_oliveiras = int(input("Digite a quantidade de oliveiras colhidas por dia: "))
    total_oliveiras += qntd_oliveiras
    
    
    if contador == 0:
        maior = menor = qntd_oliveiras
    else:
        pass
    if qntd_oliveiras > maior:
        maior = qntd_oliveiras
    elif qntd_oliveiras < menor:
        menor = qntd_oliveiras
        
    contador += 1
    
print("O total de oliveiras colhidas foi:", total_oliveiras)
print("O dia com a maior colheita foi:", maior)
print("O dia com a menor colheita foi:", menor)
        
