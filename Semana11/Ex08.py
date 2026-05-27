def conversao(hora):

    if hora == 0:
        return 12, "P.M"
    elif hora == 12:
        return 12, "A.M"
    elif hora > 12:
        return hora - 12, "P.M"
    else:
         return hora, "A.M"

def saida(hora_12, minuto, periodo):
    print("Hora convertida:", hora_12,":", minuto,  periodo)
    

def main():
    hora = int(input("Digite as horas:"))
    minuto = int(input("Digite os minutos:"))

    while hora < 0 or hora > 23:
            hora = int(input("Digite novamente as horas:"))

    while minuto < 0 or minuto > 59:
        minuto = int(input("Digite novamente os minutos:"))

    print("Antigo horário:", hora, ":", minuto)

    nova_hora, periodo = conversao(hora)
    saida(nova_hora, minuto, periodo)
    
main() 
