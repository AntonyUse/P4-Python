#!/usr/bin/python

#displayGeneralMenu :
#Titre : Gérer vos tournois d'échec

from models.object import Object
from router import Router
from models.tournamentManager import TournamentManager
from models.playerManager import PlayerManager
from models.roundManager import RoundManager
from models.gameManager import GameManager

class View(Object):
    def __init__(self):
        super().__init__()
        self.myRouter = Router()
        self.TournamentManager = TournamentManager(file='db.json', dbTable='tournaments')
        self.PlayerManager = PlayerManager(file='db.json',dbTable='players')
        self.RoundManager = RoundManager(file='db.json',dbTable='rounds')
        self.GameManager = GameManager(file='db.json',dbTable='games')
        self.homeMenu = {  # 'id':['texte du menu', 'package.module', 'classe', 'methode']
            '1':['Créer un nouveau tournoi','views.tournamentView','TournamentView','displayCreationMenu'],
            '2':['Gérer votre tournoi en cours','views.tournamentView','TournamentView','displayCurrentMenu'],
            '3':['Gérer les autres tournois','views.tournamentView','TournamentView','displayOthersMenu'],
            '4':['Gérer les joueurs','views.playerView','PlayerView','playersMenu'],
            '5':['Sortie','exit'],
        }
 
    def default(self):
        self.showMenu(self.homeMenu)

    def showMenu(self, dict):
        print("Welcome to Our Website")
        for key,value in dict.items(): # Loop to print all Choises and key of choise ! 
            print(f"{key} - {value[0]}")
        while True:
            choice = input()
            if choice in dict and dict[choice][1] != 'exit':
                print(f"{dict[choice][0]} !")
#                print(f"ca se passe ici !!!!! ====> {dict[choice][3]}")
                self.myRouter.go(dict[choice][1], dict[choice][2], dict[choice][3])()
                
            elif choice in dict and dict[choice][1] == 'exit':
                print('Au revoir !')
                exit(0)
            else:
                print('Choix inconnu')


#1. Créer un nouveau tournoi
    #1.1. Saisie des paramètres du tournoi => renvoi au menu 1.2
    #1.2. Ajouter des joueurs au tournoi
        #1.2.1. Sélection des joueurs => renvoi au menu 1.3
    #1.3. Générer le 1er Round
        #1.3.1 Génération du round => renvoi au menu principal
#2. Gérer votre tournoi en cours
    #Afficher le dernier tournoi => si la date du jour est comprise entre startingDate et endingDate d'un des tournois
    #Afficher le dernier round du tournoi s'il existe un ou des rounds
    #2.1. Sélectionner le tournoi en cours
        #2.1.1. Liste des tournois
            #2.1.1.1 Sélection du tournoi => Renvoi au menu 2
    #2.2. Sélectionner un Round du tournoi en cours
        #2.2.1. Lister les rounds du touroi
            #2.2.1.1. Sélection du round => Renvoi au menu 2
    #2.3. Créer un nouveau Round
        #2.3.1. Saisie des paramètres du Round => Génération des matchs => Renvoi au menu 2
    #2.4. Gérer les matchs
        #2.4.1. Lister les matchs du Round en cours
        #2.4.2. Saisir les scores des matchs
            #2.4.2.1. Sélection d'un match
                #2.4.2.1.1. Saisie des scores => Renvoi au menu 2.4.2
            #2.4.2.2. Revenir au menu #2.4
    #2.5. Gérer les joueurs du tournoi en cours (accessible uniquement si le 2ème round n'est pas créé, écrasera les matchs du 1er round)
        #2.5.1. Ajouter un joueur
            #2.5.1.1. Lister les joueurs
                #2.5.1.1.1. Sélection du joueur => regénération du 1er round => retour au menu 2.5.1
            #2.5.1.2. Retour au menu 2.5
        #2.5.2. Supprimer un joueur
            #2.5.2.1. Lister les joueurs
                #2.5.2.1.1. Sélection du joueur => regénération du 1er round => retour au menu 2.5.1
            #2.5.2.2. Retour au menu 2.5
    #2.6. Statistiques du tournoi en cours
        #2.6.1. Liste du classement en cours pour le dernier round du tournoi en cours
#3. Gérer les autres tournois
    #3.1. Lister les tournois
        #3.1.1. Affichage du tournoi
        #3.1.2. Retour au menu 3
    #3.2. Lister les rounds d'un tournoi
        #3.2.1. Sélection du tournoi
            #3.2.1.1. Affichage des rounds
            #3.2.1.2. Retour au menu 3.2.1.
        #3.2.2. Retour au menu 3
    #3.3. Lister les matchs d'un tournoi
        #3.3.1. Sélection du tournoi
            #3.3.1.1. Affichage des matchs
            #3.3.1.2. Retour au menu 3.3.1.
        #3.3.2. Retour au menu 3
#4. Gérer les joueurs
    #4.1. Liste des joueurs
        #4.1.1. Par ordre alphabétique
        #4.1.2. Par classement
    #4.2. Ajouter un joueur
        #4.2.1. Saisie des paramètres du joueur => Renvoir au menu 4
#5. Sortie
