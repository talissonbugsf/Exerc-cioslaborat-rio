#Faça um algoritmo que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0                       A
#  Entre 7.5 e 9.0                        B
#  Entre 6.0 e 7.5                        C
#  Entre 4.0 e 6.0                        D
#  Entre 4.0 e zero                       E
# O algoritmo deve mostrar as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))
nota_final = (n1 + n2) / 2

if nota_final >= 9 and nota_final < 10:
    print("Seu conceito é 'A' e você está APROVADO")
    print("NOTA 1:", n1, "NOTA 2:", n2)
    print("MÉDIA:", nota_final)
elif nota_final >= 7.5 and nota_final < 9:
    print("Seu conceito é 'B' e você está APROVADO")
    print("NOTA 1:", n1, "NOTA 2:", n2)
    print("MÉDIA:", nota_final)
elif nota_final >= 6 and nota_final < 7.5:
    print("Seu conceito é 'C' e você está APROVADO")
    print("NOTA 1:", n1, "NOTA 2:", n2)
    print("MÉDIA:", nota_final)
elif nota_final >= 4 and nota_final < 6:
    print("Seu conceito é 'D' e você está REPROVADO")
    print("NOTA 1:", n1, "NOTA 2:", n2)
    print("MÉDIA:", nota_final)
elif nota_final < 4 and nota_final > 0:
    print("Seu conceito é 'E' e você está REPROVADO")
    print("NOTA 1:", n1, "NOTA 2:", n2)
    print("MÉDIA:", nota_final)
else:
    print("Números inválidos.")
    
