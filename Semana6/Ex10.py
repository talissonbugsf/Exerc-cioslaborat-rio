meu_numero = int(input("Digite seu número (DE 1 a 100):"))
usuario_numero = 0

while meu_numero != usuario_numero:
    usuario_numero = int(input("Digite o número do usuário (DE 1 a 100):"))
    
    if usuario_numero < meu_numero:
        print("Há mais oliveiras, tente um número maior")
    elif usuario_numero > meu_numero:
        print("Há menos oliveiras, tente um número menor")
    elif meu_numero == usuario_numero:
        print("Parabéns! Você descobriu a quantidade de oliveiras!")
