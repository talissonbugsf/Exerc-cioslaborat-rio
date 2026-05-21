menu = 0
vetor = []

while menu != 5:
    print("MENU DE OPÇÕES:")
    print(vetor)
    print("1 - Inserir item")
    print("2- Retirar item")
    print("3 - Listar itens")
    print("4 - Retirar todos os itens")
    print("5 - Sair")

    menu = int(input("Digite uma opção do menu:"))
    
    if menu == 1:
        inserir = float(input("Inserir item:"))
        vetor.append(inserir)
    elif menu == 2:
        retirar = int(input("Retirar item:"))
        vetor.pop(retirar - 1)
    elif menu == 3:
        print("Itens:")
        for m in range (len(vetor)):
            print(vetor[m])
    elif menu == 4:
        vetor = []
    elif menu == 5:
        print("TMJ, valeu mano!")
     
