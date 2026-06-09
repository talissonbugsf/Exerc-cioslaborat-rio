def valor_kg():
    valores = []

    for v in range(5):
        valor = float(input("DIgite o valor:"))
        valores.append(valor)

    print("Ordem original:")
    print(valores)
    return valores


def main():
    valores = valor_kg()
    print("Ordem contrária:")
    for v in range(4, -1, -1):
        print(valores[v])
main()
