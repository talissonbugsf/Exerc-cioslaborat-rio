def leitura():
    codigos = []

    for v in range(15):
        codigo_RFID = int(input(f"Digite o código RFID ({len(codigos) + 1}/15): "))

        if codigo_RFID in codigos:
            print("Tente denovo.")
        else:
            codigos.append(codigo_RFID)

    return codigos

def main():
    codigos = leitura()
    print("Códigos cadastrados:")
    print(codigos)

main()
