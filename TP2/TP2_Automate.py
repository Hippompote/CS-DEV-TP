import re

dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5, "joue":3, "blanc":1, "petit":1} 
#dictionnaire de mots et leur type de mots associé 

StateTable = [
            [1,8,8,8,4,8],
            [8,1,2,8,8,8],
            [8,2,8,3,8,8],
            [5,8,8,8,7,9],
            [8,8,8,3,8,8],
            [8,5,6,8,8,8],
            [8,6,8,8,8,9],
            [8,8,8,8,8,9],
            [8,8,8,8,8,8],
            ] #table d'état de l'automate

def isPhraseValid(phrase):
    lstType = [] #on définit la liste contenant le type de chaque mot
    phrase = re.sub("[,;:\"\'\()[\]{}]]", "", phrase).replace("."," .").replace("!"," !").replace("?"," ?")
    mots = phrase.split(' ')
    for i in mots:
        i.replace('.','')
        lstType.append(dictionnaire[i])
    
    Etat = 0 #on définit l'état de départ
    for i in range(len(lstType)):
        Etat = StateTable[Etat][lstType[i]]
    if Etat == 9: #Si l'état final est 9, la phrase est valide, sinon elle ne l'est pas.
        print("Phrase valide")
    else:
        print("Phrase non valide")


phrasesTest= [
            "le joli chat joue.", 
            #"le .joli chat ; joue .",
            "la grosse souris verte mange le joli petite chat blanc.",
            "la grosse souris verte mange jean.",
            "jean joue.",
            "jean mange martin.",
            "jean mange le chat.",
            "la verte souris grosse petit mange le bleu verte chat petite."]

for p in phrasesTest:
    isPhraseValid(p)