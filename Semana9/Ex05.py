maior = 0
especial = 0
azul = 0
verde = 0
castanho = 0
loiro = 0
castanho_cabelo = 0
preto = 0
masculino = 0
feminino = 0

for contador in range(15):
    sexo_a = input("Digte seu sexo (M ou F):").upper()
    olhos_b = input("Digite a cor dos seus olhos (A, V ou C):").upper()
    cabelo_c = input("Digite a cor do seu cabelo (L, C e P):").upper()
    idade_d = int(input("Digite sua idade:"))
    
    if idade_d > maior:
        maior = idade_d
    else:
        pass
    
    if idade_d >= 18 and idade_d <= 35 and olhos_b == "V" and cabelo_c == "P":
        especial += 1
    else:
        pass
    
    if olhos_b == "A":
        azul += 1
    elif olhos_b == "V":
        verde += 1
    elif olhos_b == "C":
        castanho += 1
    
    if cabelo_c == "L":
        loiro += 1
    elif cabelo_c == "C":
        castanho_cabelo += 1
    elif cabelo_c == "P":
        preto += 1
        
    if sexo_a == "M":
        masculino += 1
    elif sexo_a == "F":
        feminino += 1
    
    p_azul = azul / 15 * (100)
    p_verde = verde / 15 * (100)
    p_castanho = castanho / 15 * (100)
    
    p_loiro = loiro / 15 * (100)
    p_castanho_cabelo = castanho_cabelo / 15 * (100)
    p_preto = preto / 15 * (100)
    
    p_masculino = masculino / 15 * (100)
    p_feminino = feminino / 15 * (100)

print("Maior idade:", )
print("Especiais:", especial)

print("Porcentagem olhos azuis:", p_azul)
print("Porcentagem olhos verdes:", p_verde)
print("Porcentagem olhos castanhos:", p_castanho)

print("Porcentagem cabelo loiro:", p_loiro)
print("Porcentagem cabelo castanho:", p_castanho_cabelo)
print("Porcentagem cabelo preto:", p_preto)

print("Porcentagem masculino:", p_masculino)
print("Porcentagem feminino:", p_feminino)


    
  

        
        
        
        
        
        
