#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import *
from datetime import datetime




jour_creation = datetime.now() 
date_naissance = jour_creation.day,jour_creation.month,jour_creation.year
heure_naissance = jour_creation.hour,jour_creation.minute
IA = dict()

def initialisation(nom,prenom,sexe):
    IA['date'] = date_naissance
    IA['heure'] = heure_naissance
    
    IA['nom'] = nom
    IA['prenom'] = prenom
    IA['sexe'] = sexe
    
    IA['faim'] = SEUIL_FAIM
    
    IA['etat'] = 'ok'

    if str(sexe) == str('une fille'):
        IA['pronom'] = str('elle')
    else:
        IA['pronom'] = str('il')
    
#------------------------------------------
# Gestion de la faim et de l'action nourrir
#------------------------------------------

# Le IA meurt quand sa caractéristique faim atteint MAX_FAIM
MAX_FAIM = 100

# Il passe à l'état 'affamé' quand sa faim dépasse SEUIL_FAIM
SEUIL_FAIM = MAX_FAIM *(38/100)



def etat():
    etat = IA['etat']
    if str(IA['faim']) <= str(0):
        etat = 'Mort !'
        print (etat,' [ETAT]')
        print('\n')
        nouveau_IA()
        
    if int(IA['faim']) >= MAX_FAIM:
        etat= 'gaver !'
        print (etat,' [ETAT]')
        print('\n')
        activite()
        
    elif IA['faim'] < SEUIL_FAIM:
        etat = 'Affamé'
        print (etat,' [ETAT]')
        print('\n')
        nourrir()
        
    else:
        print ('Ok [ETAT]')
        print('\n')
        
def nourrir():
    VALEUR_NOURRITURE = randint(5,25)
    
    FRUIT =['Abricot','Airelle','Alkékenge','Amande','Amélanche','Ananas','Arbouse','Asimine','Avocat','Banane','Bergastr(mot)e','Bigarade','Chinois','Brugnon','Canneberge','Cassis','Cerise','Châtaigne','Citron','Clémentine','Coing','Cornouiller du Canada','Cynorrhodon','Datte','Épine-vinette','Figue','Figue de barbarie','Fraise','Framboise','Grenade','Griotte','Groseille','Jujube','Kaki','Kiwi','Lime','Mandarine','Marron','Melon','Mirabelle','Mûre','Myrte','Myrtille','Nèfle','Nèfle du Japon','Noisette','Noix','Olive','Orange','Pamplemousse','Pastèque','Pêche','Pistache','Plaquebière','Chicouté','Poire','Pomme','Pomélos','Prune','Pruneau','Quetsche','Raisin']
    fruit = choice(FRUIT)
    
    IA['faim'] = IA['faim'] + VALEUR_NOURRITURE
    print (str(IA['prenom']), 'viens de manger un(e)', fruit,',qui luit à redonner +',VALEUR_NOURRITURE,'de faim.')
    

    if IA['faim'] > int(65):
        activite()
    else:
        print (str(IA['faim']),'/100 [Faim]')
        etat()

def activite():
    SPORT = ['Tennis','Basketball','Handball','Football']
    temps_activite = int(IA['faim'])*1.2
    
    temps = randint(5,round(temps_activite,0))       
    sport = choice(SPORT)

    if int(temps) >= int(200):
        consommation = randint(35,55)
    elif int(temps) > int(50) and int(temps) < int(100):
        consommation = randint(25,35)
    elif int(temps) < int(50):
        consommation = randint(2,25)
        
    seconde = int(temps*60)
 
    def decoupe(seconde):
        heure = seconde /3600
        seconde %= 3600
        minute = seconde/60
        seconde%=60
        return (heure,minute,seconde)
    
    if int(seconde) >= 3600:
        temps = decoupe(seconde)
        
        IA['faim'] = IA['faim'] - int(consommation)
        print(str(IA['prenom']),'à fait du',sport,' pendant',round(temps[0],0),'heure',round(temps[1],0),'minutes',round(temps[2],0),'secondes et ',IA['pronom'],' a dépenser ',consommation,'calories.')
        etat()
    else :
        IA['faim'] = IA['faim'] - int(consommation)
        print(str(IA['prenom']),'à fait du',sport,' pendant',temps,'minutes, et ',IA['pronom'],' a dépenser ',consommation,'calories.')
        etat()
    

    while IA['faim'] <= int(SEUIL_FAIM):
        nourrir()

    if randint(0,100) < 15:
        activite()
        
def parler():
    #
    d=input("\t>>").lower().replace(',','')
    m=d.split(" ")
    i=[0,d.split(' '),0,0]

    while str(m) !="":
        if str(len(m))=="1":
            BONJOUR = ['bonjour','salut']
            for i in range(len(BONJOUR)):
                if BONJOUR[i] == str(d):
                    print("\t>>",choice(BONJOUR))
                    d = input("\t>>").lower().replace(',','')

            AU_REVOIR = ['au revoir','Chao !','bye']
            for i in range(len(AU_REVOIR)):
                if AU_REVOIR[i] == str(d):
                    print("\t>>",choice(AU_REVOIR))
                    d = input("\t>>").lower().replace(',','')
        
        if str(len(m))>="2":
            QUESTION = ['qui','quoi','comment','combien','pourquoi','ou']
            for i in range(len(QUESTION)):
                for e in range(len(m)):
                    if QUESTION[i] == str(m[e]):
                        print(str(m[e]))
                        print("\t>>",choice(QUESTION),"?")
                        d = input("\t>>").lower().replace(',','')
        
        else:
            print(str(m))
            d = input("\t>>coucou").lower().replace(',','')
                

# Boucle de jeu
#--------------
def boucle():
    """ La boucle principale: s'il y a un IA et qu'il n'est pas mort, on l'actualise et on affiche l'animation courante """
    if IA and not IA['etat'] == 'mort':
        print (str(IA['faim']),'/100 [Faim]')
        print('\n')
        etat()
    else :
        nouveau_IA()
        
def nouveau_IA():
    """ Créé un nouveau IA. Une fenêtre de dialogue demande au joueur le nom du IA """
    aleatoire = input('Création de l\'IA aléatoire ? [oui/non]')
    if aleatoire == 'non':
        nom = input('Quel est mon nom?')
        prenom = input('Quel est mon prénom?')
        sexe = input('Quel est mon sexe? [F/M]')
        
        while nom == '':
            nom = input('Quel est mon nom?')
            
        while prenom == '':
            prenom = input('Quel est mon prénom?')

        while prenom == '':
            prenom = input('Quel est mon prénom?')

        if sexe =='F' or sexe =='f':
            sexe ='une fille'
        elif sexe == 'M' or sexe =='m':
            sexe ='un garçon'
        else :
            SEXE_DEFAULT = ['F','M']
            sexe = choice(SEXE_DEFAULT)
            if sexe =='F':
                sexe ='une fille'
            else :
                sexe ='un garçon'
        
                
    else:
        PRENOM_DEFAULT = ['Alexia','Alice','Alicia','Amélie','Anaïs','Annabelle','Arianne','Audrey','Aurélie','Camille','Catherine','Charlotte','Chloé','Clara','Coralie','','aphnée','Delphine','Elizabeth','Élodie','Émilie','Emma','Emy','Ève','Florence','Gabrielle','Jade','Juliette','Justine','Laurence','Laurie','Léa','Léanne','Maélie','Maéva','Maika','Marianne','Marilou','Maude','Maya','Mégan','Mélodie','Mia','Noémie','Océane','Olivia','Rosalie','Rose','Sarah','Sofia','Victoria','Adam','Alex','Alexandre','Alexis','Anthony','Antoine','Benjamin','Cédric','Charles','Christopher','David','Dylan','Édouard','Elliot','Émile','Étienne','Félix','Gabriel','Guillaume','Hugo','Isaac','Jacob','Jérémy','Jonathan','Julien','Justin','Léo','Logan','Loïc','Louis','Lucas','Ludovic','Malik','Mathieu','Mathis','Maxime','Michaël','Nathan','Nicolas','Noah','Olivier','Philippe','Raphaël','Samuel','Simon','Thomas','Tommy','Tristan','Victor','Vincent']
        prenom = choice(PRENOM_DEFAULT)

        NOM_DEFAULT = ['Le gall','Le bras','Guyader','Simon','Autret','Hamon','Le roux','Le roy','Herve','Salaun','Lucas','Lannuzel','Morvan','Madec','Le bars','Gueguen','Floch','Maze','Tanguy','Henry','Briand','Cariou','Kermarrec','Breton','Riou','Laurent','David','Le goff','Le guen','Jestin','Roudaut','Peron','Jacq','Durand','Quere','Stephan','Hascoet','Corre','Abiven','Lambert','Quemeneur']
        nom = choice(NOM_DEFAULT)

        SEXE_DEFAULT = ['F','M']
        sexe = choice(SEXE_DEFAULT)
        if sexe =='F':
            sexe ='une fille'
        else :
            sexe ='un garçon'      


    if prenom and nom and sexe:
        IA.clear()
        initialisation(nom,prenom,sexe)
        print ('Je m\'appelle : ',str(nom.upper()),str(prenom.capitalize()),', je suis',str(sexe))
        print ('je suis né le : ',str(date_naissance),'à',str(heure_naissance))
        print (int(IA['faim']),'/100 [Faim]')
        print('\n')

    activite()
    parler()
    

boucle()


