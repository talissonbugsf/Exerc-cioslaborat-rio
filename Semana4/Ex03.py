#Durante uma prova de corrida de rua, os atletas responderam a uma pergunta de conhecimento esportivo.
#A questão era: “Qual é a distância oficial de uma maratona?”
#Alternativas: A) 21 km, B) 42,195 km, C) 10 km, D) 5 km
#O sistema deve ler a alternativa assinalada e informar se o atleta acertou ou errou.(Resposta correta: letra B)

print("Qual é a distância oficial de uma maratona?")
print("A) 21 km")
print("B) 42,195 km")
print("C) 10 km")
print("D) 5 km")

resposta = input("Digite a sua resposta: ").upper()

if resposta == "B":
    print("Resposta correta.")
else:
    print("Resposta errada :(")
