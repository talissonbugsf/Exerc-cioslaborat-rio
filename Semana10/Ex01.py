valor = []
maior_30 = 0
soma_30 = 0
soma = 0

for v in range (0,8):
    valores = int(input("Digite o valor:"))
    valor.append(valores)
    soma = soma + valor[v]

    if valores >= 30:
        soma_30 = soma_30 + valor[v]
        maior_30 += 1
    else:
        pass

print("Números maiores que 30:", maior_30)
print("Soma dos números maiores que 30:", soma_30)
print("Soma de todos os números:", soma)
