valor = []
maior_30 = 0
soma = 0

for v in range (0,8):
    valores = int(input("Digite o valor:"))
    valor.append(valores)
    soma = soma + valor[v]

    if valores >= 30:
        maior_30 = maior_30 + valor[v]
    else:
        pass

print("Soma dos números maiores que 30:", maior_30)
print("Soma de todos os números:", soma)
