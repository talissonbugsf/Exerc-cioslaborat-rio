def leitura():
    azeitonas = []

    for v in range(6):
        azeitona = float(input("Digite os KG de azeitona por lote:"))
        azeitonas.append(azeitona)

    return azeitonas

def rendimento(azeitonas):
    multi = 0.18

    for v in range(6):
        multiplicacao = azeitonas[v] * multi
        print("Lote", v + 1, ":", azeitonas[v], "KG", multiplicacao)


def main():
    azeitonas = leitura()
    rendimento(azeitonas)

main()
