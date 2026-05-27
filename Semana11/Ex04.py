def laranxinha(laranjas_compradas):

    if laranjas_compradas <= 12:
        la = laranjas_compradas * 0.40
        return la
    
    elif laranjas_compradas > 12:
        la = laranjas_compradas * 0.25
        return la

def main():
    laranjas_compradas = int(input("Quantidades de laranjas compradas:"))
    laranxinha(laranjas_compradas)
    la = laranxinha(laranjas_compradas)
    print("Valor da compra: R$ ", la)

main()
