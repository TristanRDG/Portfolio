# coding: utf-8 
from tkinter import *
from math import *





###FONCTIONS###------------------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------------------------------------
### PREMIER TOUR - 0.5 ###  /Permet de définir qui est le premier a joueur grace au bouttons/
#-----------------------------------------------------------------------------------------------------------------------------------------

def yellow ():
    global tour_précédent, premier_tour, partie_commencer
    tour_précédent = 1 #red#
    premier_tour = 0
    plateau (x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, L, ResX, ResY)
    RED.pack_forget()
    YELLOW.pack_forget()
    partie_commencer = True
    Can.bind("<ButtonRelease-1>", tour_joueur)
    
            #-----------------------------------------------------------------------#

def red ():
    global tour_précédent, premier_tour, partie_commencer
    tour_précédent = 0 #yellow#
    premier_tour = 1
    plateau (x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, L, ResX, ResY)
    RED.pack_forget()
    YELLOW.pack_forget()
    partie_commencer = True
    Can.bind("<ButtonRelease-1>",tour_joueur)

#-----------------------------------------------------------------------------------------------------------------------------------------
### TOUR JOUEUR - 01 ###  /Définnie qui joue se tour ci/
#-----------------------------------------------------------------------------------------------------------------------------------------
    
def tour_joueur (event):
    global tour_précédent, nombre_tour
    XS=event.x
    YS=event.y

    numero = Can.find_overlapping(XS,YS,XS,YS)[0]

    
    if numero != None:
        ###numero = int((numero+1)/2)   /!\
        if tour_précédent == 1:
            Can.itemconfigure(dictionnaire_hexagone["hexagone_" + str(numero)], fill="#facf5a")#yellow#
            if nombre_tour ==2 and hex_rouge[0] in hex_jaune:
                del hex_jaune[0]
            if nombre_tour > 0:
                del dictionnaire_hexagone["hexagone_" + str(numero)] 
            liste_noire.append(numero)
            verifie_victoire (0, numero, False, False)
            
        else:
            Can.itemconfigure(dictionnaire_hexagone["hexagone_" + str(numero)], fill="#ff5959")#red#
            if nombre_tour ==2 and hex_jaune[0] in hex_rouge:
                del hex_rouge[0]
            if nombre_tour > 0: 
                del dictionnaire_hexagone["hexagone_" + str(numero)] 
            liste_noire.append(numero) 
            verifie_victoire (1, numero, False, False)

#-----------------------------------------------------------------------------------------------------------------------------------------
### VERIFIE VICTOIRE - 02 ###  /Vérifie si le dernier joueur à avoir jouer a gagner ou non/
#-----------------------------------------------------------------------------------------------------------------------------------------

def verifie_victoire (tour_précédent, numero, flag_1, flag_2):
    
    if tour_précédent == 0: #yellow#

        if numero in nord:
            flag_1 = True
        if numero in sud:
            flag_2 =True
        if flag_1 == True and flag_2 == True:
            entre_jeux(tour_précédent, True)
        
        
        for i in range(7):

            if numero in est and i<3:
                continue
            elif numero in ouest and i>2 and i<5:
                continue
            elif numero in sud and i>4 and i<1:
                continue
            elif numero in nord and i>1 and i<4:
                continue
            
            if i==6:
                if len(possible) > 0:
                    numero = possible[-1]
                    del possible[-1]
                    verifie_victoire(tour_précédent, numero, flag_1, flag_2)
                else:
                    entre_jeux(tour_précédent, False)
                
            elif numero + hexa_adja[i] in hex_jaune:
                possible.append(numero + hexa_adja[i])
                hex_jaune.remove(numero + hexa_adja[i])
                liste_noire.append(numero + hexa_adja[i])
                continue
            else:
                continue

                          #-------------------------------------------------------------#
            
    else: #red#

        if numero in est:
            flag_1 = True
        if numero in ouest:
            flag_2 =True
        if flag_1 == True and flag_2 == True:
            entre_jeux(tour_précédent, True)
        
        for i in range(7):
            
            if numero in est and i<3:
                continue
            elif numero in ouest and i>2 and i<5:
                continue
            elif numero in sud and i>4 and i<1:
                continue
            elif numero in nord and i>1 and i<4:
                continue
            
            if i==6:
                if len(possible) > 0:
                    numero = possible[-1]
                    del possible[-1]
                    verifie_victoire(tour_précédent, numero, flag_1, flag_2)
                else:
                    entre_jeux(tour_précédent, False)
    
            elif numero + hexa_adja[i] in hex_rouge:
                possible.append(numero + hexa_adja[i])
                hex_rouge.remove(numero + hexa_adja[i])
                liste_noire.append(numero + hexa_adja[i])
                continue
            else:
                continue      
                  
#-----------------------------------------------------------------------------------------------------------------------------------------
### ENTRE JEUX - 03 ###  /définie s'il faut annoncer une victoire ou lancer le prochain tour/      
#-----------------------------------------------------------------------------------------------------------------------------------------

def entre_jeux (tp, condition_victoire):
    global tour_précédent, premier_tour, nombre_tour, VR, VJ

    nombre_tour += 1

    if condition_victoire == True:
        dictionnaire_hexagone.clear()
        bouton_rejouer.pack()
        global victoire
        victoire = True
        gagner_lbl.pack()
        return

            
    for i in range (len(liste_noire)) :

        if tp == 1:
            hex_rouge.append(liste_noire[0])
            del liste_noire[0]
            
        else:
            hex_jaune.append(liste_noire[0])
            del liste_noire[0]

            
    tour_précédent = tp

#-----------------------------------------------------------------------------------------------------------------------------------------      
### PLATEAU ###  /Création du plateau de jeux/
#-----------------------------------------------------------------------------------------------------------------------------------------
        
def plateau (x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, L, ResX, ResY):

    x_rond = x0 #sauvegarde des coordonnées pour plus loin dans la fonction#
    y_rond = y0

    X = x4  
    Y = y4

    N = 0 
        
    for ligne in range (11):
        
        if ligne != 0:            
            x0 = X
            y0 = Y
            x1=x0 + (L/2)/tan(radians(30))
            y1=y0 - L/2
            x2=x1 + (L/2)/tan(radians(30))
            y2=y0
            x3=x2
            y3=y0 + L
            x4=x1 
            y4=y3 + L/2
            x5=x0
            y5=y3
            
        for colone in range (11):
            if ligne != 0 and colone == 0:
                X = x4
                Y = y4

            N += 1 
            dictionnaire_hexagone["hexagone_" + str(N)] = Can.create_polygon([(x0,y0), (x1,y1), (x2,y2), (x3,y3), (x4,y4), (x5,y5)], outline="black", fill="#103c42") 
            #Can.create_text(x0, y0, text=str(N), fill="white") #/!\

                     
            x0 += ((L/2)/tan(radians(30)))*2  
            y0 = y0
            x1=x0 + (L/2)/tan(radians(30))
            y1=y0 - L/2
            x2=x1 + (L/2)/tan(radians(30))
            y2=y0
            x3=x2
            y3=y0 + L
            x4=x1 
            y4=y3 + L/2
            x5=x0
            y5=y3
            
    
    x=x_rond+L #*3 /!\'
    y=ResY/2  #+4*L /!\'
    Can.create_oval(x-L, y-L, x+L, y+L, fill="#ff5959", outline="") #red#
    x=ResX-(x_rond+L)#*3) /!\'
    y=ResY/2  #-4*L /!\'
    Can.create_oval(x-L, y-L, x+L, y+L, fill="#ff5959", outline="") #red#
    x=(ResX/2)-4.5*L
    y=y_rond/2
    Can.create_oval(x-L, y-L, x+L, y+L, fill="#facf5a", outline="") #yellow#
    x=(ResX/2)+4.5*L
    y=ResY-(y_rond/2)
    Can.create_oval(x-L, y-L, x+L, y+L, fill="#facf5a", outline="") #yellow#

#-----------------------------------------------------------------------------------------------------------------------------------------
### Rejouer ### /Permet de relancer la partie, réinnitialise les variables/
#-----------------------------------------------------------------------------------------------------------------------------------------
        
def rejouer():
    global nombre_tour, premier_tour, partie_commencer, victoire

    nombre_tour = 0
    premier_tour = None
    partie_commencer = False
    victoire = False
    
    liste_noire.clear()
    hex_jaune.clear()
    hex_rouge.clear()

    bouton_rejouer.pack_forget()
    RED.pack()
    YELLOW.pack()
    RED['state'] =  NORMAL
    YELLOW['state'] =  NORMAL
    gagner_lbl.pack_forget()

#-----------------------------------------------------------------------------------------------------------------------------------------
### Quitter ###  /Affiche les boutons approprier et cache les autre, permet de quitter/ 
#-----------------------------------------------------------------------------------------------------------------------------------------

def quitter ():

    sure_lbl.pack()
    
    if RED['state'] ==  NORMAL and YELLOW['state'] ==  NORMAL:
        RED.pack_forget()
        YELLOW.pack_forget()
        RED['state'] =  DISABLED
        YELLOW['state'] =  DISABLED
    if bouton_rejouer['state'] ==  NORMAL:
        bouton_rejouer.pack_forget()
        bouton_rejouer['state'] =  DISABLED
    buton_oui.pack()
    buton_non.pack()
    
#-----------------------------------------------------------------------------------------------------------------------------------------
### Retour ###  /r'affiche les bouttons approprier et cache les autres, continue le jeux/
#-----------------------------------------------------------------------------------------------------------------------------------------

def retour ():
    global nombre_tour, victoire, sure_lbl 

    sure_lbl.pack_forget()
    
    if RED['state'] ==  DISABLED and YELLOW['state'] ==  DISABLED and partie_commencer == False:
        RED.pack()
        YELLOW.pack()
        RED['state'] =  NORMAL
        YELLOW['state'] =  NORMAL
    if bouton_rejouer['state'] ==  DISABLED and victoire == True:
        bouton_rejouer.pack()
        bouton_rejouer['state'] =  NORMAL
    buton_oui.pack_forget()
    buton_non.pack_forget()


################----------------------------------------------------------------------------------------------------------------
###PRGMPRCPL###----------------------------------------------------------------------------------------------------------------
################----------------------------------------------------------------------------------------------------------------

fenetre = Tk()

ResX = 800 #Résolution# 
ResY = 600

fenetre.geometry=("ResX x ResY")
fenetre.configure(bg="#103c42")
fenetre.title=("HEXGAME")

Can=Canvas(fenetre, bg ="#02576c", height=ResY-10, width=ResX)
Can.pack()

###VARIABLES GLOBALS/Listes/dictionnaiers...###--------------------------------------------------------------------------

###Listes###------------------------------------------------------------------------------------------
nord = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ]
sud = [111 ,112 ,113 ,114 ,115 ,116 ,117 ,118 ,119 ,120 ,121 ]
est = [11 ,22 ,33 ,44 ,55 ,66 ,77 ,88 ,99 ,110 ,121 ]
ouest = [1 ,12 ,23 ,34 ,45 ,56 ,67 ,78 ,89 ,100 ,111 ]
hexa_adja = [-10 ,1 ,11 ,10 ,-1 ,-11 ]
hex_jaune=[]
hex_rouge=[]
possible=[]
liste_noire=[]

###Dictionnaire###---------------------------------------------------------------------------------

dictionnaire_hexagone = {}

###Variables###------------------------------------------------------------------------------------

L= ResY / 30 #longueur X0 X5 et X2 X3 (taile de l'hexagone)
nombre_tour = 0
tour_précédent = None 
premier_tour = None
victoire = False
partie_commencer = False

###Boutons###---------------------------------------------------------------------------------------

RED=Button(fenetre, text= "rouge", width=10, command=red, bg="#ffeaa5")
YELLOW=Button(fenetre, text="jaune", width=10,  command=yellow, bg="#ffeaa5")
bouton_rejouer = Button(fenetre, text = "Rejouer", width=10,  command=rejouer, bg="#ffeaa5")
bouton_quitter = Button(fenetre, text = "quitter", width=10,  command=quitter, bg="#099a97")
buton_oui = Button(fenetre, text = "oui", width=10, command=fenetre.destroy, bg="#ffeaa5")
buton_non = Button(fenetre, text = "non", width=10,  command=retour, bg="#ffeaa5")
RED.pack()
YELLOW.pack()
bouton_rejouer.pack_forget()
bouton_quitter.pack(side='left', padx=10, pady=10)
buton_oui.pack_forget()

###Labels###-----------------------------------------------------------------------------------------

sure_lbl = Label(fenetre, text="Etes vous sur ?", width=12, font=('Arial', 10, 'bold'), bg="#ffeaa5")
gagner_lbl = Label(fenetre, text="VICTOIRE", font=('Arial', 20, 'bold'), bg="#ffeaa5")
sure_lbl.pack_forget()
gagner_lbl.pack_forget()

###Coordonnées Hexagones###------------------------------------------------------------------

#######
x0=((ResX / 2) -14*L) #Coordonées de#
y0=((ResY / 2) -8.2*L)  #début de grille#
x1=(x0 + (L/2)/tan(radians(30)))
y1=(y0 - L/2)
x2=(x1 + (L/2)/tan(radians(30)))
y2=y0
x3=x2
y3=(y0 + L)
x4=x1 
y4=(y3 + L/2)
x5=x0
y5=y3
#######
fenetre.mainloop
#######

###-Volia-BELLEVILLE--Tristan-MAURIN--TS2--2019--BAC-ISN-###
