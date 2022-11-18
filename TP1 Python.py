def is_bissextile(annee):

    print(annee%400 == 0 or (annee%4 == 0 and annee%100 != 0))

annee_s = int(input("Veuillez entrer l'année"))

is_bissextile(annee_s)