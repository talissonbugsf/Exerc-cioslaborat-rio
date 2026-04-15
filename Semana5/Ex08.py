caixa_atual = float(input("Digite o dinheiro do caixa atual:"))
contador = 1

while contador <= 4:
    opcao = int(input("Selecione uma opção do caixa:"))
    
    if opcao == 1:
        print("Você selcionou a opção: Realizar venda")
        venda = float(input("Digite o valor da venda: R$ "))
        caixa_atual = caixa_atual + venda
    elif opcao == 2:
        print("Você selecionou a opção: Retirar dinheiro")
        retirar = float(input("Digite quanto você quer retirar: R$ "))
        caixa_atual = caixa_atual - retirar
    elif opcao == 3:
        print("Você selecionou a opção: Dinheiro em caixa")
        print("Seu caixa atual é:", caixa_atual)
    elif opcao == 4:
        print("Até mais!")
    else:
        print("Opção inválida")
        
    contador += 1
    
