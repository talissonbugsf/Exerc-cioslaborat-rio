contador = 0
km = 500

while km > 0:
    if km >= 80:
        km = km - 80
        contador += 1
        print("Hora ", contador, ", O caminhão percorreu 80 km. Faltam ", km, "km")
    elif km < 80:
        contador += 1
        print("Hora ", contador, ", O caminhão percorreu ", km, " km. Faltam 0 km")
        km = km - km
        print("Entrega concluída com sucesso!")
