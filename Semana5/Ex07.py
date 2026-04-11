contador = 1
qntd_cafe = 0
qntd_cappuccino = 0
qntd_cha = 0

while contador <= 10:
    bebida = input("Digite sua bebida favorita(A/B/C):").upper()
    
    if bebida == "A":
        qntd_cafe += 1
    elif bebida == "B":
        qntd_cappuccino += 1
    elif bebida == "C":
        qntd_cha += 1
    else:
        print("Opção inválida.")
    
    total = qntd_cafe + qntd_cappuccino + qntd_cha
    cafe_porcentagem = (qntd_cafe / total) * 100
    cappuccino_porcentagem = (qntd_cappuccino / total) * 100
    cha_porcentagem = (qntd_cha / total) * 100
    
    contador += 1
    
    
print("Votos para café(A)", qntd_cafe)
print("Votos para cappuccino(B)", qntd_cappuccino)
print("Votos para chá(C)", qntd_cha)
print("Porcentagem de votos para café:", cafe_porcentagem)
print("Porcentagem de votos para cappuccino:", cappuccino_porcentagem)
print("Porcentagem de votos para chá:", cha_porcentagem)
    
