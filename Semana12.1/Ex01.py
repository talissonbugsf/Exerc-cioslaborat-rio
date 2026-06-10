def leitura():
    lotes = []

    for v in range(5):
        lote = int(input("Valor de lote:"))
        lotes.append(lote)

    print("Ordem Original:")
    
    for i in range(5):
        print(lotes[i])
    
    return lotes

def inverso(lotes):
    print("Ordem contrária:")
    for v in range(4, -1, -1):
        print(lotes[v]) 

def main():
    lotes = leitura()
    inverso(lotes)

main()
