def is_bissextile(annee):

    print(annee%400 == 0 or (annee%4 == 0 and annee%100 != 0))


def nb_jours(mois,annee):

    if mois == 2 and is_bissextile(annee):
        return 29
    elif mois == 2:
        return 28
    elif mois in [4,6,9,11]:
        return 30
    else:
        return 31

def is_date_valid(jour,mois,annee):
    return (jour > 0 and jour < nb_jours(mois,annee) and is_mois_valid(mois,annee))

def is_mois_valid(mois,annee):
    return ( 0 < mois <=12 )


jour_s = int(input("Veuillez entrer un jour"))
mois_s = int(input("Veuillez entrer un mois"))
annee_s = int(input("Veuillez entrer l'annee"))
is_bissextile(annee_s)
print(nb_jours(mois_s,annee_s))
print(is_date_valid(jour_s,mois_s,annee_s))