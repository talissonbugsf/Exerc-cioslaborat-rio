contador = 1
salario_ate_10000 = 0
qntd_ata = 0
qntd_def = 0
salario_total = 0

while contador <= 10:
    idade = int(input("Digite a idade do jogador:"))
    posicao = str(input("Digite sua posição (A/D):")).upper()
    salario = float(input("Digite seu salário:"))
    
    salario_total += salario
 
    if contador == 1:
        mais_novo = idade
        mais_velho = idade
    else:
        if idade < mais_novo:
            mais_novo = idade
        
        if idade > mais_velho:
            mais_velho = idade
    
    if posicao == "A":
        qntd_ata = qntd_ata + 1
        if salario <= 10000:
            salario_ate_10000 = salario_ate_10000 + 1
        else:
            pass
            
    elif posicao == "D":
        qntd_def = qntd_def + 1
    else:
        print("Código inválido")
        
    contador += 1
        
    
    media = salario_total / 10
    
    
print("A média salarial dos jogadores é: R$", media)
print("O jogador mais novo tem ", mais_novo, "anos e o mais velho tem ", mais_velho, "anos.") 
print("A quantidade de atacantes com salário de até R$ 10.000 é:", salario_ate_10000) 
print("A quantidade de atacantes é: ", qntd_ata, "e a quantidade de defensores é:", qntd_def)
    
