#Um cinema está automatizando a venda de ingressos. O sistema deve ler o valor base do ingresso e a opção escolhida pelo cliente:
#1 - Ingresso normal (valor cheio), 2 - Estudante (50% de desconto), 3 - Criança até 12 anos (paga 40% do valor), 4 - Idoso (paga 60% do valor)
#O programa deve calcular e mostrar o valor a ser pago.

valor = float(input("Digite o valor do ingresso: "))
print("Tipos de cliente: 1 - Ingresso normal, 2 - Estudante (50% de desconto), 3 - Criança até 12 anos (paga 40% do valor), 4 - Idoso (paga 60% do valor)")

opcao = int(input("Escolha qual tipo de cliente você se insere: "))

if opcao == 1:
    print("Você pagará:", valor, "R$")
elif opcao == 2:
    valor_final = valor / 2
    print("Você pagará:", valor_final, "R$")
elif opcao == 3:
    valor_final = valor * 0.40
    print("Você pagará:", valor_final, "R$")
elif opcao == 4:
    valor_final = valor * 0.60
    print("Você pagará:", valor_final, "R$")
else:
    print("Opção inválida")
