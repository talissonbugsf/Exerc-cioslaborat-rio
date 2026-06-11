import random

def colheita():
    acoes = []

    for v in range(5):
        acao = float(input("Forças de ação da equipe:"))
        acoes.append(acao)

    return acoes

def pragas():
    resistencias = []

    while len(resistencias) < 5:
        resistencia = float(random.randint(1, 100))

        if resistencia not in resistencias:
            resistencias.append(resistencia)
        else:
            pass
    
    return resistencias

def confronto(acoes, resistencias):
    ganhamos = 0
    perdemos = 0

    for v in range(5):
        if acoes[v] > resistencias[v]:
            ganhamos += 1
        else:
            perdemos += 1

    print("Equipe da colheita:", acoes)
    print("Equipe da praga:", resistencias)
    print("Resultado final:", ganhamos, "vezes que vencemos;", perdemos, "vezes que perdemos.")



def main():
    acoes = colheita()
    resistencias = pragas()
    confronto(acoes, resistencias)

main()
