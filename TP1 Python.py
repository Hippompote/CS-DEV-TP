def is_bissextile(annee):
    bissextile = False
    if annee%400 == 0 or (annee%4 == 0 and annee%100 != 0):
        print("L'année est bissextile")
    else:
        print("L'année n'est pas bissextile")

annee = int(input("Veuillez entrer l'année"))

is_bissextile(annee)