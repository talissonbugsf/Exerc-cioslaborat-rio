def media_kg ():

    valores = []
    media = 0

    for v in range(8):
        valor = float(input("Digite o valor:"))
        valores.append(valor)
        media = media + valores[v]

    media = (media) / 8
    return valores, media

def main():
      
    valores, media = media_kg()

    print("Média em KG:", media)
    print("Produções acima da média:")

    for valor in valores:
        if valor > media:
            print(valor)

main()
