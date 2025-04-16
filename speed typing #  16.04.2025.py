"speed typing program" or "programme de course d'écriture sur le clavier" # 16.04.2025

import time
from tkinter import *
from threading import Thread

# initialiser les variables
words = [ # liste de touts les mots
    "chat", "chien", "maison", "voiture", "arbre", "rivière", "montagne", "mer", "ciel",
    "lune", "étoile", "soleil", "nuage", "pluie", "vent", "neige", "glace", "feu", "eau",
    "terre", "pierre", "sable", "roche", "bois", "herbe", "fleur", "arbre", "fruit", "légume",
    "pomme", "poire", "raisin", "banane", "orange", "citron", "carambole", "mangue", "kiwi",
    "papaye", "fraise", "cerise", "myrtille", "framboise", "mûre", "chocolat", "café", "thé",
    "lait", "beurre", "fromage", "pain", "baguette", "croissant", "pâte", "riz", "pâtes",
    "sauce", "soupe", "salade", "gratin", "tarte", "gâteau", "crème", "glace", "sorbet",
    "jus", "sirop", "soda", "bière", "vin", "champagne", "rhum", "whisky", "vodka",
    "cognac", "liqueur", "cocktail", "smoothie", "milkshake", "eau gazeuse", "eau plate",
    "eau minérale", "eau de source", "eau de mer", "eau de pluie", "eau de rivière", "eau de lac",
    "eau de puits", "eau de robinet", "eau de bouteille", "eau de fontaine", "eau de cascade"
]
rtime = 60 # temps demandé (en seconde)
nowword = 0


# créer l'interface
root = Tk()
root.title('prgramme de course d\'écriture pour le clavier')
wlabel = Label(root,font=('Arial',16)) # label où les mots seront affichés
wlabel.pack()
entry = Entry(root,font=('Arial',20),justify='center') # entrée où on écrit les mots
entry.pack()

# créer les fonctions nécessaire

def endgame():
    pass # à faire

def chronometer():# fonction pour suivre le temps demandé puis faire le jeu
    time.sleep(rtime)
    root.unbind_all()
    
    endgame()

def begin():# réinitialiser le jeu
    global nowword
    nowword = 0
    wlabel.configure(text=words[0])
    entry.delete(0,'end')

def compare():# vérifier si ce qu'on a tapé correspond au mot demandé
    if entry.get() == words[nowword]:
        return True
    else:
        return False

def next():# passer à la question suivante
    # si on arrive à la fin de la liste, cela créerait une erreur "list out of range" alors il faut faire une liste de mots (variable word) suffisamment grande
    global nowword
    nowword += 1
    wlabel.configure(text=words[nowword])
    entry.delete(0,'end')

def badanswer():
    entry.configure(fg='red')
    root.update()
    root.after(1750,entry.delete(0,'end'))
    entry.configure(fg='black')

def click_enter(event):
    if compare():
        next()
    else:
        badanswer()
# connecter les fonctions avec l'interface
root.bind('<Return>',click_enter)

# lancement de l'interface
begin()
root.mainloop()