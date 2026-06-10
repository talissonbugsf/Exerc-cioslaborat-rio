def leitura():
    arvores = []

    for v in range(5):
        arvore = int(input("Produção da árvore:"))
        arvores.append(arvore)

    return arvores

def maior_menor(arvores):
    maior = 0
    menor = 0
    ma = 0
    me = 0

    for v in range(len(arvores)):

        if v == 0:
            maior = arvores[v]
            menor = arvores[v]
            ma = v
            me = v

        else:
            if arvores[v] > maior:
                maior = arvores[v]
                ma = v
            elif arvores[v] < menor:
                menor = arvores[v]
                me = v
    
    print("Maior:", maior, " - ", ma)
    print("Menor:", menor, " - ", me)


def main():
    arvores = leitura()
    maior_menor(arvores)

main()
