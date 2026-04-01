#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#
#                              Até 5 Kg                 Acima de 5 Kg
#    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#    Maçã              R$ 1,80 por Kg          R$ 1,50 por Kg
#
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = float(input("Digite a quantidade em kg de morangos:"))
maca = float(input("Digite a quantidade em kg de maçãs:"))

if morango <= 5:
    valormo = morango * 2.50
elif morango > 5:
    valormo = morango * 2.20

if maca <= 5:
    valorma = maca * 1.80
elif maca > 5:
    valorma = maca * 1.50
    
valor = valorma + valormo
kg = morango + maca

if valor > 25 or kg > 8:
    valor_final = valor * 0.90
    print("O valor final da sua compra é: R$", valor_final)
else:
    valor_final = valor
    print("O valor final da sua compra é: R$", valor_final)
