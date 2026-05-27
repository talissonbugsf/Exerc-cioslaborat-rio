def aprovado (media):
    print("Aprovado!")

def recuperacao (media):
    print("Recuperação!")

def reprovado (media):
    print("Reprovado")

def main():
    soma_notas = 0
    for n in range(5):
        notas = float(input("Digite a nota:"))
        soma_notas = soma_notas + notas
    media = soma_notas / 5
    print("Média final:", media)

    if media >= 7:
        aprovado (media)
    
    elif media >= 4 and media < 7:
        recuperacao (media)

    elif media < 4:
        reprovado (media)

main()
