from importlib import import_module
from mailbox import NotEmptyError


a = "Benvenuti al casinò di Ottavio"
b = "Per giocare creare un account"
c = "Inserisci i dati richiesti"
print(a)
print(b)
print(c)

d = input ("Nome:  ")
e = input ("Cognome: ")
f = input ("Età:")

print(input)

if (len(d)) > 2: 
 print("Accettato")
else:
 print("Paramentro non corretto")

if (len(e)) > 2:
    print("Accettato")
else:
    print(type(e) and ("Paramentro non corretto"))    