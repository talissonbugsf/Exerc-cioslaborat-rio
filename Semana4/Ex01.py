#Faça um algoritmo que leia a pontuação de dois times em uma partida. Mostre qual time venceu, qual perdeu ou se houve empate.

ponto1 = int(input("Digite a pontuação do time 1: "))
ponto2 = int(input("Digite a pontuação do time 2: "))

if ponto1 > ponto2:
    print("O time 1 ganhou e o 2 perdeu.")
elif ponto1 < ponto2:
    print("O time 2 ganhou e o 1 perdeu.")
else:
    print("Ocorreu um empate.")
