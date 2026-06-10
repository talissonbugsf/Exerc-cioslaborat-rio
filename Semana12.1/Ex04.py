def qntd():
    azeitonas = []

    for v in range(5):
        azeitona = int(input("Quantidades de azeitonas em KG:"))
        azeitonas.append(azeitona)
    
    return azeitonas

def soma_media(azeitonas):
    soma = 0
    media = 0

    for v in range(5):
        soma += azeitonas[v]
        media = soma / 5

    print("Soma:", soma)
    print("Média:", media)

def main():
    azeitonas = qntd()
    soma_media(azeitonas)

main()
