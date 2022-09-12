#!/usr/bin/python

from webbrowser import get
from views.view import View
from models.player import Player

class PlayerView(View):
    def __init__(self):
        super().__init__()

    def playersMenu(self):
        thisMenu = {  # 'id':['texte du menu', 'package.module', 'classe', 'methode']
            '1':['Lister les joueurs','views.playerView','PlayerView','displayAllPlayers'],
            '2':['Ajouter un joueur','views.playerView','PlayerView','create'],
            '3':["Modifier les données d'un joueur",'views.playerView','PlayerView','update'],
            '4':['Supprimer un joueur','views.playerView','PlayerView','delete'],
            '5':['Revenir au menu principal','views.view','View','default'],
        }
        self.showMenu(thisMenu)

    def addToTournament(self):
        self.displayAll()
        print("Numéro du ou des joueur(s) à ajouter ? (séparés par une virgule, laisser vide pour revenir au menu)")
        list = input()
        if (list):
            doc_ids = list.split(',')
            currentTourney = self.TournamentManager.getLast()
            self.myRouter.go('controllers.playerController','PlayerController','addToTournament')(doc_ids,currentTourney.getId())
        else:
            self.myRouter.go('views.tournamentView','TournamentView','displayCreationMenu')()



    def displayAll(self):
        for player in self.PlayerManager.getAll():
            print(f"{player.getId()} : {player.getName()} {player.getFirstname()}")
        
    def displayAllPlayers(self):
        self.displayAll()
        self.playersMenu()

    def create(self):  # id,name,firstname,birthdate,gender,level
        print("Nom du joueur ?")
        name = input()
        print("Prénom ?")
        firstname = input()
        print("Date de naissance ?")
        birthdate = str(input())
        print("Genre ? (M ou F)")
        gender = input()
        print("Niveau du joueur ?")
        level = int(input())

        createPlayerMethod = self.myRouter.go('controllers.playerController','PlayerController','create')
        if (createPlayerMethod(name, firstname, birthdate, gender, level)):
            print("Joueur créé !")
            self.playersMenu()
        else:
            print('Problème à la saisie des données')

    def update(self):  # id,name,firstname,birthdate,gender,level
        self.displayAll()
        print("Indiquez le numéro du joueur que vous souhaitez éditer :")
        id = input()
        print("Laissez vides et tapez sur Entrée pour les champs que vous ne souhaitez pas modifier !")
        print(f"Nom du joueur ?")
        name = input()
        print("Prénom ?")
        firstname = input()
        print("Date de naissance ?")
        birthdate = str(input())
        print("Genre ? (M ou F)")
        gender = input()
        print("Niveau du joueur ?")
        level = input()

        updatePlayerMethod = self.myRouter.go('controllers.playerController','PlayerController','update')
        if (updatePlayerMethod(id, name, firstname, birthdate, gender, level)):
            print("Joueur mis à jour !")
            self.playersMenu()
        else:
            print('Problème à la saisie des données')

    def delete(self):  # id,name,firstname,birthdate,gender,level
        self.displayAll()
        print("Indiquez le numéro du joueur que vous souhaitez éditer :")
        id = input()

        if (id):
            deletePlayerMethod = self.myRouter.go('controllers.playerController','PlayerController','delete')
            if (deletePlayerMethod(id)):
                print("Joueur supprimé !")
                self.playersMenu()
            else:
                print('Problème à la saisie des données')
        else:
                print("Pas d'id de joueur saisi, retour au menu !")
                self.playersMenu()
