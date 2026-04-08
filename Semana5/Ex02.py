codigo_brinquedo = 1
carrinho = 0

while codigo_brinquedo != 0:
    
    codigo_brinquedo = int(input("Digite o código do produto: "))
     
    if codigo_brinquedo == 1040:
        
        carrinho = carrinho + 1
        print(" Quantidade de vezes que o código 1040 foi digitado: ", carrinho)

    elif codigo_brinquedo == 0:
        print("Processo encerrado")
        print("Quantidade de vezes que o código 1040 foi digitado: ", carrinho)
