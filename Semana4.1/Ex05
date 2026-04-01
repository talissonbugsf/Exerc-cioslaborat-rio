#A cidade está prestes a sediar a Corrida Anual dos Campeões, e os organizadores precisam saber se você está preparado para participar. Um programa fará 5 perguntas sobre sua preparação:
#Você treinou regularmente nas últimas semanas? Participou de treinos longos (acima de 10 km)? Seguiu uma dieta especial para a corrida? Já competiu em provas oficiais neste ano? Conta com acompanhamento de treinador ou equipe?
#De acordo com suas respostas "Sim" ou "Não", o sistema deve classificá-lo:
#2 respostas positivas → Você é classificado como Participante Casual (ainda precisa de mais treino).
#3 ou 4 respostas positivas → Você é classificado como Atleta Competitivo (tem boas chances de se destacar).
#5 respostas positivas → Você é classificado como Atleta de Elite (pronto para o pódio!).
#Menos de 2 respostas positivas → Você é classificado como Não Preparado (talvez seja melhor assistir da arquibancada este ano).

r = str(input("Você treinou regularmente nas últimas semanas?: ")).upper()
l = str(input("Participou de treinos longos (acima de 10 km)?: ")).upper()
d = str(input("Seguiu uma dieta especial para a corrida?: ")).upper()
c = str(input("Já competiu em provas oficiais neste ano?: ")).upper()
t = str(input("Conta com acompanhamento de treinador ou equipe?: ")).upper()

if r == "SIM":
    p = 1
else:
    p = 0
if l == "SIM":
    po = 1
else:
    po = 0
if d == "SIM":
    pon = 1
else:
    pon = 0
if c == "SIM":
    pont = 1
else:
    pont = 0
if t == "SIM":
    ponto = 1
else:
    ponto = 0

pontos = p + po + pon + pont + ponto
print("Seus pontos:", pontos)

if pontos < 2:
    print("Você é classificado como Não Preparado (talvez seja melhor assistir da arquibancada este ano).")
elif pontos == 2:
    print("Você é classificado como Participante Casual (ainda precisa de mais treino).")
elif pontos >= 3 and pontos <= 4:
    print("Você é classificado como Atleta Competitivo (tem boas chances de se destacar).")
elif pontos == 5:
    print("Você é classificado como Atleta de Elite (pronto para o pódio!).")
    
