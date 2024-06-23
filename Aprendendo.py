nome = str(input("Qual seu nome?"))
nota = float(input("Qual foi sua nota na prova?"))

if nota >= 6:
    print ("Você foi bem,",nome)
elif nota == 5.9:
    print ("Foi quase lá",nome)
else:
    print ("tu é burro",nome)