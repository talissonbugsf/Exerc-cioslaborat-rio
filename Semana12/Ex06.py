def fazenda():
    A = []
    B = []

    for v in range(4):
        proA = int(input("Prdoução da fazenda A:"))
        A.append(proA)
    for v in range(4):
        proB = int(input("Prdoução da fazenda B:"))
        B.append(proB)

    return A, B, v

def soma_fazenda(A, B):
    soma = []

    for v in range(4):
        total = A[v] + B[v]
        soma.append(total)

    return soma

def main():
    A, B, v = fazenda()
    resultado = soma_fazenda(A, B)

    print("Produção por lote:")
    print(resultado)

main()
