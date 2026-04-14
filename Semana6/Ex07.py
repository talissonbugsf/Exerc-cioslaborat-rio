contador = 0
idade_total = 0

while contador != 15:
    idade = int(input("Digite sua idade:"))
    idade_total += idade
    
    media = idade_total / 15
    
    contador += 1

if media <= 25:
        print("A turma se classifica como: Turma jovem")
elif media >= 26 and media <= 60:
        print("A turma se classifica como: Turma adulta")
elif media > 60:
        print("A turma se classifica como: Turma idosa")
else:
        pass
    
