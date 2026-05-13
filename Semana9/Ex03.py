par = 0
impar = 0
zero = 0

for contador in range(10):
    numero = int(input("Digite o número:"))
    if numero % 2 == 0:
        par += 1
    elif numero % 2 != 0:
        impar += 1
    if numero == 0:
        zero += 1
    else:
        pass
print("Pares:", par)
print("Ímpares:", impar)
print("Zeros:", zero)
    
