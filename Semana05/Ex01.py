valor = 0
opcao = 0
qntd_ingressos = 100 

while opcao != 4:
    print("1 – Vender ingresso")
    print("2 – Adicionar ingressos extras")
    print("3 – Mostrar ingressos disponíveis")
    print("4 – Encerrar")
    opcao = int(input("Selecione uma opção: "))
    
    if opcao == 1:
        valor_ingresso = float(input("Digite o valor do ingresso: "))
        compra_ingressos = int(input("Digite a quantidade de ingressos: "))
        valor = valor_ingresso * compra_ingressos
        qntd_ingressos = qntd_ingressos - compra_ingressos
        print("A quantidade de ingressos comprados foram:", compra_ingressos,)
        print("O valor da sua compra foi: R$ ", valor)
        
    elif opcao == 2:
        qntd_extra = int(input("Digite a quantidade de ingressos que deseja adicionar: "))
        qntd_ingressos = qntd_ingressos + qntd_extra
        print("A nova quantidade de ingressos é: ", qntd_ingressos)
    
    elif opcao == 3:
        ingressos_vendidos = int(input("Digite a quantidade de ingressos vendidos: "))
        ingressos_dispo = qntd_ingressos - ingressos_vendidos
        print("A quantidade de ingressos restantes é: ", ingressos_dispo)
        
    elif opcao == 4:
        print("Até mais! Sua compra teve o valor de: R$", valor)
        
    else:
        print("Opção inválida.")
        
