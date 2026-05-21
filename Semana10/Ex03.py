valor = []

for v in range (0, 10):
    numero = float(input("Digite o número:"))
    valor.append(numero)

print("Números pares:")

for v in range (len(valor)):
    if valor[v] % 2 == 0:
        print("Valor", v+ 1, "=", valor[v])
