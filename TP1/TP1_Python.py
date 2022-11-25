def is_bissextile(annee):

    return(annee%400 == 0 or (annee%4 == 0 and annee%100 != 0))


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

def mesImpots(revenu):
    tranches = [10225,26070,74545,160336]
    if revenu < 0:
        return False
    elif revenu <= tranches[0]:
        return 0
    elif tranches[0]+1 < revenu < tranches[1]:
        return (revenu-tranches[0]*0.11)
    elif tranches[1]+1 < revenu < tranches[2]:
        return(((revenu-(tranches[1])+1)*0.3) + (tranches[1]-tranches[0])*0.11)
    elif tranches[2]+1 < revenu < tranches[3]:
        return((revenu-tranches[2]+1)*0.41 + (tranches[2]-tranches[1])*0.3 + (tranches[1]-tranches[0])*0.11)
    else:
        return((revenu-tranches[3]+1)*0.44 + (tranches[3]-tranches[2])*0.41 + (tranches[2]-tranches[1])*0.3 + (tranches[1]-tranches[0])*0.11)

'''impots = int(input("Entrez votre revenu en €: "))

print(mesImpots(impots))'''

import numpy as np



def multiplication(A,B):
    C = [[0 for k in range(len(A[0]))] for k in range(len(B))] 
    for i in range(len(A)):
        for j in range(len(B)):

            for k in range(len(A[0])):
                C[i][j]+=(A[i][k]*B[k][j])
    return C


