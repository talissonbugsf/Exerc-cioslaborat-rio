valor = []
maior_100 = 0

for v in range (0, 10):
    numero = float(input("Digite o número:"))
    valor.append(numero)

    if numero > 100:
        maior_100 += 1
    else:
        pass

print("Quantos números são maiores que 100:", maior_100)

for v in range (len(valor)):
    if valor[v] > 100:
        print("Valor ", v + 1, "=", valor[v])



