plantacao_A = 80000
plantacao_B = 200000
anos = 0

while plantacao_A < plantacao_B:
    
    plantacao_A += plantacao_A * 0.03
    plantacao_B += plantacao_B * 0.015
    
    anos += 1
    
print("A quantidade de anos para a plantação A ultrapassar a B é:", anos)
