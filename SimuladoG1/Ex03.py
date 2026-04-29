nome = str(input("Digite o nome da transportadora:"))
saldo = float(input("Digite o saldo inicial: R$ "))
caminhao = 1
opcao = 0

while saldo <= 0:
    saldo = float(input("Digite um saldo positivo: R$ "))
    
while opcao != 5:
    opcao = int(input("Digite uma opção: "))
    if  opcao == 1:
        entrega = int(input("Digite a quantidade de entregas:"))
        valor_entrega = entrega * 1200
        saldo = saldo + valor_entrega
    elif opcao == 2:
        caminhao_add = int(input("Digite a quantidade de caminhões que deseja adicionar:"))
        custo_caminhao = caminhao_add * 30000
        if saldo >= custo_caminhao:
            saldo = saldo - custo_caminhao
            caminhao = caminhao + caminhao_add
        else:
            print("Você não tem saldo para comprar:", caminhao_add, "caminhão(ões)")
    elif opcao == 3:
        print("Você tem ", caminhao," caminhão(ões)")
    elif opcao == 4:
        manutencao = 3000
        if saldo >= manutencao:
            saldo = saldo - manutencao
        else:
            print("Você não tem saldo para fazer uma manutenção")
    elif opcao == 5:
        print("Seu saldo final é: R$ ", saldo)
        print("E o total de caminhões que você tem é:", caminhao)
        print("Você escolheu a opção: sair")
