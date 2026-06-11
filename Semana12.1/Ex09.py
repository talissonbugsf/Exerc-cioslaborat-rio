import random

def leitura():
    codigos = []

    for v in range(10):
        codigo = random.randint(1, 100)
        codigos.append(codigo)

    print("Números escolhidos:", codigos)

    return codigos

def pares(codigos):
    pares = 0

    for codigo in codigos:
        if codigo % 2 == 0:
            pares += 1
        else:
            pass

    print("Números pares:", pares)


def main():
    codigos = leitura()
    pares(codigos)

main()
