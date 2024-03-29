from random import randint

mots = open('../TP3/Mots.txt','r')



def randWord(liste):
    str = liste.read()
    lstMots = str.split(' ')
    return(lstMots[randint(0,len(lstMots)-1)])

def isWin(word):
    Victoire = False
    if '_' not in word:
        Victoire = True
    return Victoire

def playAgain(word):
    if isWin(word) == True:
        print('Victoire !')
        playAgain = input('Voulez vous rejouer ? (o = oui; n = non)')
        if playAgain == 'o':
            pendu(randWord(mots))
        else:
            return

def pendu(mot):
    life = 8
    print(mot)
    guessWord  = mot[0]
    for i in range(len(mot)-1):
        guessWord += '_'
    print(guessWord)

    triedLetters = []
    while '_' in guessWord:
        guess = input('Proposez une lettre:')
        triedLetters.append(guess)

        for i,l in enumerate(mot):
            if l == guess:
                guessWord= guessWord[:i] + l + guessWord[i+1:]

        if guess in mot:
            print('Bien joué !')
            print(guessWord)    
            
        else:
            life = life -1
            print('Hé bien non !')
            print(guessWord)
            if life ==0:
                print("Pendu !")
                return
        
        print('Nombre de chances restantes:', life)
        print('Lettres déjà essayées:', triedLetters)
    playAgain(guessWord)
pendu(randWord(mots))
