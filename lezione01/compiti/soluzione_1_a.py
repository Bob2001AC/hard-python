print("Benvenuti al casinò da Bob\n")
print("Per giocare è neccessario un account\n")
print("Inserisci i dati richiesti\n")

nome = input("Nome: ")
cognome = input("Cognome: ")
eta = input("Età: ")

if len(nome) > 1 and len(cognome) > 1 and int(eta) >= 18:
    print("I dati inseriti sono validi")
    print("Il nome inserito è: " + nome)
    print("Il cognome inserito è: " + cognome)
    print("L'età inserita è: " + eta)
else:
    print("I dati non sono corretti")
    
string = nome
nome= string.capitalize()
print(nome)
string = cognome
cognome= string.capitalize()
print(cognome)
