def somaImposto (taxaImposto, custo):
    taxa = taxaImposto / 100
    com_imposto = (taxa * custo) + custo
    return com_imposto

def main():
    porcentagem = float(input("Digite a porcentagem de impostos:"))
    valor = float(input("Digite o valor do produto: R$ "))
    somaImposto(porcentagem, valor)
    com_imposto = somaImposto(porcentagem, valor)
    print("Antigo valor de custo: R$", valor)
    print("Novo valor de custo: R$:", com_imposto)


main()
