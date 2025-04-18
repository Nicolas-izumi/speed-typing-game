"speed typing program" or "programme de course d'écriture sur le clavier" # 16.04.2025

import time
from random import shuffle
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
timer = Label(root,text=repr(rtime),font='KristenITC 30',fg='dark blue')
timer.pack(anchor='nw')
wlabel = Label(root,font=('Arial',16)) # label où les mots seront affichés
wlabel.pack(side='top')
entry = Entry(root,font=('Arial',20),justify='center') # entrée où on écrit les mots
entry.pack()

# créer les fonctions nécessaire

def endgame():# fonction pour dire que c'est la fin du temps et demander si on veux recommencer
    root.unbind_all('<Return>')# désactiver les touches
    # effacer tout ce qu'on a écrit
    entry.delete(0,'end')
    wlabel.configure(text='')
    
    # faire un menu de pour demander ce quel'on veux faire dans un menu à part
    top = Toplevel(root)
    top.title('options')
    
    explicationL = Label(top,text='Le temps s\'est écoulé')# label pour expliquer ce qui s'est passé
    explicationL.pack(fill='x',expand=True)
    
    frame = Frame(top)# frame pour placer les boutons "recommencer" et "quitter"
    frame.pack(fill='x',expand=True)

    restart = Button(frame,text='recommencer',command=lambda:[top.destroy(), begin(),chronometer()])# bouton refaire le jeu
    restart.grid(row=0,column=0,ipadx=5,ipady=5)
    quit_button = Button(frame,text='quitter',command=root.destroy)# bouton quitter le jeu
    quit_button.grid(row=0,column=1,ipadx=5,ipady=5)

def chronometer():# fonction arrêter le jeu au temps demandé
    for i in range(rtime,-1,-1):# faire le décompte de rtime jusqu'à 0 inclus
        time.sleep(1)
        timer.configure(text=i)# met à jour le chronomètre après 1s
        root.update()# met à jour la fenêtre root
    
    endgame()# active la fonction pour la fin de jeu

def begin():# réinitialiser le jeu
    global nowword
    
    # connecter les fonctions avec l'interface
    root.bind('<Return>',click_enter)

    # initialiser les variables
    nowword = 0
    wlabel.configure(text=words[0])
    entry.delete(0,'end')

def compare():# vérifier si ce qu'on a tapé correspond au mot demandé
    if entry.get() == words[nowword]:
        return True
    else:
        return False

def next():# passer à la question suivante
    # si on arrive à la fin de la liste (ce qui n'arrivera probablement pas), cela créerait une erreur "list out of range" alors il faut faire une liste de mots (variable word) suffisamment grande
    global nowword
    nowword += 1
    wlabel.configure(text=words[nowword])
    entry.delete(0,'end')

def badanswer():# fonction pour montrer que c'est faut, puis effacer ce qu'on a écrit
    entry.configure(fg='red')
    root.update()
    root.after(1750,entry.delete(0,'end'))
    entry.configure(fg='black')

def click_enter(event):# Quand on clique sur la touche 'Enter', cette fonction sera activée.
    # compare ce qu'on a écrit avec le mot demandé:
    if compare():
        next()# passe au mot suivant
    else:
        badanswer()# dit que c'est faux

# lancement de l'interface
begin()
t = Thread(target=chronometer)
t.start()
root.mainloop()
print('end\n')
