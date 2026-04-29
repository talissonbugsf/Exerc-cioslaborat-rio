valor_carga = float(input("Digite o valor da carga: R$ "))
destino = int(input("Digite o destino (Berlim = 1, Lisboa = 2 e Paris = 3):"))

while destino < 1 or destino > 3:
    destino = int(input("Digite o destino (Berlim = 1, Lisboa = 2 e Paris = 3):"))
if destino == 1:
    valor_total = valor_carga * 1.05
    print("O valor a ser cobrado é:", valor_total)
elif destino == 2:
    valor_total = valor_carga * 1.07
    print("O valor a ser cobrado é:", valor_total)
elif destino == 3:
    while valor_carga < 10000:
        valor_carga = float(input("Digite o valor da carga: R$ "))
    valor_total = valor_carga * 1.10
    print("O valor a ser cobrado é:", valor_total)
