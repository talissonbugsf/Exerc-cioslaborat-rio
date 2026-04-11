caixa_atual = float(input("Digite o dinheiro do caixa atual:"))
contador = 1

while contador <= 4:
    opcao = int(input("Selecione uma opção do caixa:"))
    
    if opcao == 1:
        print("Você selcionou a opção: Realizar venda")
    elif opcao == 2:
        print("Você selecionou a opção: Retirar dinheiro")
    elif opcao == 3:
        print("Você selecionou a opção: Dinheiro em caixa")
        print("Seu caixa atual é:", caixa_atual)
    elif opcao == 4:
        print("Até mais!")
    else:
        print("Opção inválida")
        
    contador += 1
    
