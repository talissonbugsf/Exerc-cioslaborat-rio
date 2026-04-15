idade = 0
while idade < 1 or idade > 150:
    idade = int(input("Digite sua idade: "))
    if 1 <= idade <= 150:
        print("Sua idade é:", idade)
    else:
        print("Idade inválida, digite novamente.")

salario = 0
while salario <= 0:
    salario = float(input("Digite o seu salário: R$ "))
    if salario > 0:
        print("Seu salário é: R$", salario)
    else:
        print("Salário inválido, digite novamente.")

sexo = ""
while sexo != "f" and sexo != "m":
    sexo = input("Digite seu sexo (f ou m): ").lower()
    if sexo == "f" or sexo == "m":
        print("Seu sexo é:", sexo)
    else:
        print("Sexo inválido, digite novamente.")

estado = ""
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
    estado = input("Digite seu estado civil (s, c, v ou d): ").lower()
    if estado == "s" or estado == "c" or estado == "v" or estado == "d":
        print("Seu estado civil é:", estado)
    else:
        print("Estado civil inválido, digite novamente.")
