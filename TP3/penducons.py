from random import randint
from tkinter import Tk, Label,Button,StringVar,Entry,Canvas
mots = open('./TP3/Mots.txt','r')

fen = Tk()
fen.title('Jeu du pendu')
fen.geometry('1280x720')
fen.configure(bg = 'gray')
hangCanvas = Canvas(fen)
l = Label(fen, text="Entrez une lettre")
l.pack(side = 'left')

e = Entry(fen, bd = 5)
e.pack(side = 'left')

Valider = Button(fen, text='Valider')
Valider.pack(side='left')
fen.mainloop()

def randWord(liste):
    str = liste.read()
    lstMots = str.split(' ')
    return(lstMots[randint(0,len(lstMots)-1)])

def isWin(word):
    Victoire = False
    if '_' not in word:
        Victoire = True
    return Victoire

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
        if guess in triedLetters:
            guess = input('Lettre déjà proposée !')
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
        
    if isWin(guessWord) == True:
        print('Victoire !')
        '''playAgain = input('Voulez vous rejouer ? (o = oui; n = non)')
        if playAgain == 'o':
            pendu(randWord(mots))
        else:
            return
'''
pendu(randWord(mots))

