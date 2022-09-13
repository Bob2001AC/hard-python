from tkinter import N


print("Benvenuti al casinò da Bob")
"\n"
print("Per giocare è neccessario un account")
"\n"
print("Inserisci i dati richiesti")
"\n"

a = input("Nome: ")
b = input("Cognome: ")
c = input("Età: ")
print(input)

if (len(a)) and (len(b)) > 1 and int(c) >= 18:
 print("I dati inseriti sono validi")
else: 
 print("Inserire nuovamente i dati: ")
