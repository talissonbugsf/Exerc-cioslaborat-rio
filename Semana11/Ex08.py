def conversao(hora):
    hora_12 = hora - 12
    return hora_12

def saida(hora_12, minuto):
    hora_12 = conversao (hora_12)
    print("Nova hora:", hora_12, ":", minuto)

def main():
    hora = int(input("Digite as horas:"))
    if hora < 12 and hora > 23:
        while hora < 12 or hora > 23:
            hora = int(input("Digite novamente as horas:"))
    else:
        pass
    minuto = int(input("Digite os minutos:"))
    conversao(hora)
    saida(minuto)
    

main()
