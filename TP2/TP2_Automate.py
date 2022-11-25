dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

StateTable = [[1, 8, 4, 8, 8, 8],
            [8, 2, 8, 8, 1, 8],
            [8, 8, 8, 3, 2, 8],
            [5, 8, 7, 8, 8, 9],
            [8, 8, 8, 3, 8, 8],
            [8, 6, 8, 8, 5, 8],
            [8, 8, 8, 8, 6, 9],
            [8, 8, 8, 8, 8, 9]]


inputTable = list(dictionnaire.keys())

OutTable = [8,9]


def isPhraseValid(phrase):
    mots = phrase.split(' ')
    for i in mots:
        if i not in inputTable:
            print("Phrase incorrecte, le mot" + i +"ne fais pas partie de la liste")
        else:
            j = dictionnaire[i]
            for k in range(len(StateTable[j])):
                if StateTable[j][k] == 9:
                    print("phrase correcte")
                else:
                    print("Phrase incorrecte")

phrasetest = input("Entrez une phrase valide")

isPhraseValid(phrasetest)
