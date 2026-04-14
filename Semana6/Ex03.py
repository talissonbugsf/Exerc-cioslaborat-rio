numero_oliveiras = int(input("Digite o número de oliveiras a serem plantadas:"))
numero_fileiras = int(input("Digite o número de fileiras disponíveis:"))

divisao = numero_oliveiras / numero_fileiras
sobra = numero_oliveiras % numero_fileiras
print("Quantas oliveiras ficarão em cada fileira:", divisao)
print("Quantas mudas sobrarão:", sobra)
