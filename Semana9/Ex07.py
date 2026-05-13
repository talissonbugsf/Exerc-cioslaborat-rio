menor = int(input("Digite o número menor:"))
maior = int(input("Digite o número maior:"))

while menor >= maior:
  print("O primeiro número deve ser menor.")
  menor = int(input("Digite o número menor:"))
  maior = int(input("Digite o número maior:"))
 
 
print("Pares:") 
for contador in range(menor, maior + 1):
  if contador % 2 == 0:
    print(contador)
  else:
    pass
