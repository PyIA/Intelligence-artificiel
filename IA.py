#!/usr/bin/python3
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
    
    IA['faim'] = 50
    
    IA['etat'] = 'ok'
    
#------------------------------------------
# Gestion de la faim et de l'action nourrir
#------------------------------------------

# Le IA meurt quand sa caractéristique faim atteint MAX_FAIM
MAX_FAIM = 100
# Il passe à l'état 'affamé' quand sa faim dépasse SEUIL_FAIM
SEUIL_FAIM = MAX_FAIM *(40/100)
# L'action nourrir diminue la faim de VALEUR_NOURRITURE
VALEUR_NOURRITURE = MAX_FAIM *(30/100)

def etat():
    etat = IA['etat']
    if str(IA['faim']) < str(0):
        etat = 'Mort !'
        print (etat,' [ETAT]')
        nouveau_IA()
    if int(IA['faim']) >= MAX_FAIM:
        etat= 'gaver !'
        print (etat,' [ETAT]')
    elif IA['faim'] < SEUIL_FAIM or IA['faim'] == '0':
        etat = 'Affamé'
        print (etat,' [ETAT]')
    else:
        print ('Ok [ETAT]')
        
def nourrir():
    IA['faim'] = IA['faim'] + VALEUR_NOURRITURE
    print (str(IA['faim']),'/100 [Faim]')
    print (SEUIL_FAIM,'     [SEUIL_FAIM]')
    print (VALEUR_NOURRITURE,'     [VALEUR_NOURRITURE] \n -------')
    etat()

def activite():
    TIME = ['1','10','15','30']
    SPORT = ['Tennis','Basketball','Handball','Football']
    CONSOMMATION = ['25','50','75']

    temps = choice(TIME)
    sport = choice(SPORT)
    consommation = choice(CONSOMMATION)

    IA['faim'] = IA['faim'] - int(consommation)
    print(str(IA['prenom']),'à fait du',sport,' pendant',temps,'minutes, et il a dépenser ',consommation,'calories.')
    print (str(IA['faim']),'/100 [Faim]')
    etat()
    
def apprendre():

#--------------
# Boucle de jeu
#--------------
def boucle():
    """ La boucle principale: s'il y a un IA et qu'il n'est pas mort, on l'actualise et on affiche l'animation courante """
    if IA and not IA['etat'] == 'mort':
        print (str(IA['faim']),'/100 [Faim]')
        print (SEUIL_FAIM,'     [SEUIL_FAIM]')
        print (VALEUR_NOURRITURE,'     [VALEUR_NOURRITURE] \n -------')
        etat()
    else :
        nouveau_IA()

def nouveau_IA():
    """ Créé un nouveau IA. Une fenêtre de dialogue demande au joueur le nom du IA """
    aleatoire = input('Création de l\'IA aléatoire ? [oui/non]')
    faim = str(50)
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


    if prenom and nom and sexe and faim:
        IA.clear()
        initialisation(nom,prenom,sexe)
        print ('Je m\'appelle : ',str(nom),str(prenom),', je suis',str(sexe))
        print ('je suis né le : ',str(date_naissance),'à',str(heure_naissance))
        print (str(faim),'/100 [Faim]')
    

boucle()


