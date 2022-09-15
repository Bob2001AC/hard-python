print("\n")
print("- - - Welcome to the casinò - - -\n")
print(" - - -Enter the required data to create your account - - -\n")
list_language=["Italian","English"]
#LanguageOne = "Italian"
#LanguageTwo = "English"
LanguageSelect= input("Select LAnguage:  ")

while list_language[0] or list_language[1] :
    print("The language select is  :"+LanguageSelect)
#if LanguageSelect == len(list_language[0] or list_language[1]):#LanguageOne and LanguageTwo :
    #print("The language select is:  " + LanguageSelect)
#else:
    #print("The language selcet is not aviable")
   

    if LanguageSelect == list_language[0]:#LanguageOne :
        nameA=input("Nome:  ")
        surnameA=input("Cognome:  ")
        ageA=input("Età:  ")
    if len(nameA)>1 and len(surnameA) >1 and int(ageA) >= 18:
        print("Dati accettati")
    else:
        print("Dati non validi")

    if LanguageSelect == list_language[1]:#LanguageTwo :
        nameB=input("Name:  ")
        surnameB=input("Surname")
        ageB=input("Age:  ")
    if len(nameB)>1 and len(surnameB)>1 and int(ageB)>= 18:
        print("Accepted data")
    else:
        print("Invalid data")

