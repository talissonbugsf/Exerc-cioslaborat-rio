def menu():
    print("1 - Sacar")
    print("2- Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = int(input("Digite uma opção:"))
    return opcao

def mostrar_saldo(saldo):
    print("Seu saldo atual é:", saldo)

def sacar(saldo):
    valor = float(input("Quanto deseja sacar: R$ "))
    if valor <= saldo:
        saldo -= valor
        mostrar_saldo(saldo)
    else:
        print("Saldo insuficiente.")
    return saldo

def depositar(saldo):
    valor = float(input("Digite o quanto deseja depositar:"))
    saldo += valor
    mostrar_saldo(saldo)
    return saldo


def main():
    opc = 0
    saldo = 0

    while opc != 4:
        opc = menu() #opc = opcao

        if opc == 1:
            saldo = sacar(saldo)
        
        elif opc == 2:
            saldo = depositar(saldo)
        
        elif opc == 3:
            mostrar_saldo(saldo)

        elif opc == 4:
            print("Tchau pra ti meu galo veio!")
        



main()
