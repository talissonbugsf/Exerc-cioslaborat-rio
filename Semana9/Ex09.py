a = 0
b = 0
c = 0

for contador in range(20):
    jornal = input("Digite seu jornal preferido:").upper()
    
    if jornal == "A":
        a += 1
    elif jornal == "B":
        b += 1
    elif jornal == "C":
        c += 1
        
ap = a / 20 * (100) 
bp = b / 20 * (100)
cp = c / 20 * (100)
    
if ap <= bp and ap <= cp:
    print("O jornal menos lido é o A, com ", ap, "%")
    if bp <= cp:
        print("seguido pelo B, com ", bp, "%")
        print("e o mais lido é o C, com ", cp, "%")
    else:
        print("seguido pelo C, com ", cp, "%")
        print("e o mais lido é o B, com ", bp, "%")

elif bp <= ap and bp <= cp:
    print("O jornal menos lido é o B, com ", bp, "%")
    if ap <= cp:
        print("seguido pelo A, com ", ap, "%")
        print("e o mais lido é o C, com ", cp, "%")
    else:
        print("seguido pelo C, com ", cp, "%")
        print("e o mais lido é o A, com ", ap, "%")
        
elif cp <= ap and cp <= bp:
    print("O jornal menos lido é o C, com ", cp, "%")
    if ap <= bp:
        print("seguido pelo A, com ", ap, "%")
        print("e o mais lido é o B, com ", bp, "%")
    else:
        print("seguido pelo B, com ", bp, "%")
        print("e o mais lido é o A, com ", ap, "%")
