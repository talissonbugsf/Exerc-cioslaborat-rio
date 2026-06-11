def leitura():
    codigos = []
    codigo = 0

    for v in range(10):
        codigo = float(input("Digite o código RFID:"))

        while codigo <= 1000:
            codigo = float(input("Digite novamente o código RFID: "))

        codigos.append(codigo)

    return codigos

def main():

    codigos = leitura()
    print("Códigos validados:", codigos)

main()
