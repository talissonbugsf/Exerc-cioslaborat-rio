def c ():
    codigos = []

    for v in range(5):
        codigo = int(input("Digite o código:"))
        codigos.append(codigo)

    return codigos

def inspecao ():
    confirmar = int(input("Digite o codigo de produto:"))

    return confirmar

def main ():
    lista = c()
    busca = inspecao()

    if busca in lista:
        print("Encontrado.")
    else:
        print("Não encontrado.")

main()
