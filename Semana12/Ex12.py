def elemento():
    kg_colhidos = []
    preco_por_kg = []

    for e in range(5):
        kg = float(input("Digite o kg:"))
        kg_colhidos.append(kg)
        preco = float(input("Digite o preço:"))
        preco_por_kg.append(preco)

    return kg_colhidos, preco_por_kg

def multi(kg_colhidos, preco_por_kg):
    multiplicacao = []

    for e in range(5):
        resultado = kg_colhidos[e] * preco_por_kg[e]
        multiplicacao.append(resultado)

    return multiplicacao

def main():
    kg_colhidos, preco_por_kg = elemento()
    resultado = multi(kg_colhidos, preco_por_kg)

    print("Produção por árvore:")
    print(resultado)

main()
