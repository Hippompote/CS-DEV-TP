from tkinter import Tk, Label,Button,StringVar,Entry,Canvas
import penducons as pc

mots = open('./TP3/Mots.txt','r')

def penduGraph():
    pc.pendu(pc.randWord(mots))

fen = Tk()
fen.title('Jeu du pendu')
fen.geometry('600x600')
fen.configure(bg = 'gray')
hangCanvas = Canvas(fen)
l = Label(fen, text="Entrez une lettre")
l.pack(side = 'left')

e = Entry(fen, bd = 5)
e.pack(side = 'left')

Valider = Button(fen, text='Valider', command=penduGraph())
Valider.pack(side='right')
fen.mainloop()




