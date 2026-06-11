import random

def IDs():
    codigos = []

    for v in range(10):
        codigo = random.randint(1, 50)
        codigos.append(codigo)

    print("Números:", codigos)

    return codigos

def selecao(codigos):
    par = 0
    impar = 0

    for codigo in codigos:
        if codigo % 2 == 0:
            par += 1
        else:
            impar += 1

    print("Pares:", par)
    print("Ímpares:", impar)


def main():
    codigos = IDs()
    selecao(codigos)

main()
