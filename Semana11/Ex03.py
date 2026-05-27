def dobro(valor):
    d = valor * 2
    print("O dobro do valor é:", d)
    return d

def triplo(valor):
    t = valor * 3
    print("O triplo do valor é:", t)
    return t

def main():
    valor = float(input("Digite um número:"))
    dobro(valor)
    triplo(valor)

main()
