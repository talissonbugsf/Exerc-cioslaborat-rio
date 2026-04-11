contador = 1
total_tempo = 0
menos30 = 0
entre30e60 = 0

while contador <= 7:
    tempo = float(input("Digite o tempo do corredor: "))
    
    total_tempo += tempo
    
    if tempo < 30:
        menos30 += 1
        
    elif tempo >= 30 and tempo <= 60:
        entre30e60 += 1
        
    contador += 1
        
media = total_tempo / 7
percent = (entre30e60 / 7) * 100
    
print("Tempo médio dos corredores: ", media, "min")
print("Corredores que terminaram em menos de 30 min: ", menos30)
print("Porcentagem de corredores que terminaram entre 30 e 60 min: ", percent, "%")
