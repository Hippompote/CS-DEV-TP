from TP1_Python import is_date_valid

jour = int(input("Veuillez entrer un jour"))
mois = int(input("Veuillez entrer un mois"))
annee = int(input("Veuillez entrer une année"))

if is_date_valid(jour,mois,annee):
    print("La date est valide")
else:
    print("La date est non valide")