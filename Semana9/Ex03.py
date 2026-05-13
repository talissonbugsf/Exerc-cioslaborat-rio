primeiro_numero = 0
outro_numero = 1

for contador in range(1, 11):
    print(contador, primeiro_numero)
    
    fibonacci = primeiro_numero + outro_numero
    primeiro_numero = outro_numero
    outro_numero = fibonacci
