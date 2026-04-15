idade_oliveira = int(input("Digite a idade da oliveira:"))
altura = idade_oliveira * 30

if altura >= 500:
    print("Oliveira adulta")
elif altura < 500:
    print("Oliveira em crescimento")
