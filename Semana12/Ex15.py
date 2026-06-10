def menu():
    print("MENU: LOTES DEVEM SER PARES.")
    print("1 - Inserir lote")
    print("2 - Listar lotes")
    print("3 - Retirar um lote")
    print("4 - Limpar todos os lotes")
    print("5 - Contar quantos lotes têm produção maior que X (X informado pelo usuário)")
    print("6 - Verificar se um código está presente")
    print("7 - Encontrar maior e menor código no array")
    print("8 - Sair")


def main():
    lotes = []
    opcao = 0

    while opcao != 8:
        menu()
        opcao = int(input("Digite uma opção do menu:"))
        if opcao == 1:
            inserir = int(input("Insira um valor de lote:"))
            if inserir % 2 == 0:
                lotes.append(inserir)
            else:
                print("Erro.")
        
        elif opcao == 2:
            print("Lista de lotes:", lotes)

        elif opcao == 3:
            retirar = int(input("Lote que deseja tirar:"))
            if retirar in lotes:
                lotes.remove(retirar)
            else:
                print("Não encontrado.")


        elif opcao == 4:
            lotes.clear()

        elif opcao == 5:
            contador = 0
            x = int(input("Digite um valor de 'X':"))
            for y in lotes:   
                if y > x:
                    contador += 1
                else:
                    pass
            print("Quantidade de lotes > x:", contador)

        elif opcao == 6:
            buscar = int(input("Digite um valor para a busca:"))
            if buscar in lotes:
                print("Encontrado.")
            else:
                print("Não encontrado.")

        elif opcao == 7:
            if len(lotes) == 0:
                print("Sem lotes.")
            else:
                maior = max(lotes)
                menor = min(lotes)
                print("Maior código:", maior)
                print("Menor código:", menor)

        elif opcao == 8:
            print("Até mais!!!")

main()
