def notas(nota1, nota2):
    media_notas = (nota1 + nota2) / 2
    return media_notas

def situacao(media_notas):
    if media_notas >= 7:
        print("Você foi aprovado!")
    else:
        print("Você foi reprovado!")

def main():
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    media = notas(nota1, nota2)
    situacao(media)
    print("Média:", media)
    print(situacao)


main()
