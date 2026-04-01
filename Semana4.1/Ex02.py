#Um engenheiro quer verificar se três forças podem manter um corpo em equilíbrio. Faça um programa que leia três valores correspondentes às forças. O sistema deve verificar se elas obedecem à condição de equilíbrio (a soma de duas deve ser maior que a terceira). Caso positivo, classifique o equilíbrio como:
#Simétrico → três forças iguais, Parcialmente simétrico → duas forças iguais, Assimétrico → três forças diferentes, Caso contrário, informe que não há equilíbrio.

força1 = float(input("Digite o valor da primeira força:"))
força2 = float(input("DIgite o valor da segunda força:"))
força3 = float(input("Digite o valor da terceira força:"))

if força1 + força2 > força3 and força1 + força3 > força2 and força2 + força3 > força1:
    print("Essas forças tem condição de equilíbrio")
    if força1 == força2 == força3:
        print("Essa condição de equilíbrio é simétrica")
    elif força1 == força2 or força1 == força3 or força2 == força3:
        print("Essa condição de equilíbrio é parcialmente simétrica")
    else:
        print("Essa condição de equilíbrio é assimétrica")
else:
    print("Essas forças não possuem condição de equilíbrio")
