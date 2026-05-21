valor_a = []
valor_b = []

for v in range (0, 10):
    numero_a = float(input("Digite o número:"))
    valor_a.append(numero_a)

for v in range (len(valor_a)):
    inverso = -1 - v
    valor_b.append(valor_a[inverso])
    
print("Ordem original", valor_a)
print("Ordem inversa", valor_b)
