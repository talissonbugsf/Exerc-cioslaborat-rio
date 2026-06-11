def leitura():
    codigos = []

    for v in range(5):
        codigo = int(input("Códigos de lote:"))
        codigos.append(codigo)

    return codigos

def verificador(codigos):
    if len(codigos) == len(set(codigos)):
        print("Distintos")
    else:
        print("Há duplicadas")

def main():
    codigos = leitura()
    verificador(codigos)

main()
