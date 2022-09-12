#!/usr/bin/python

from views.view import View

class TournamentView(View):
    def __init__(self):
        super().__init__()

    def displayCreationMenu(self):
        thisMenu = {  # 'id':['texte du menu', 'package.module', 'classe', 'methode']
            '1':['Créer le tournoi','views.tournamentView','TournamentView','create'],
            '2':['Ajouter les joueurs','views.playerView','PlayerView','addToTournament'],
            '3':['Générer le 1er Round','views.roundView','RoundView','createFirst'],
            '4':['Revenir au menu principal','views.view','View','default'],
        }
        self.showMenu(thisMenu)

    def displayCurrentMenu(self):
        thisMenu = {  # 'id':['texte du menu', 'package.module', 'classe', 'methode']
            '1':['Sélectionner le tournoi en cours','views.tournamentView','TournamentView','selectCurrentTournament'],
            '2':['Sélectionner un Round du tournoi en cours','views.tournamentView','TournamentView','selectCurrentRound'],
            '3':['Créer un nouveau Round','views.roundView','RoundView','createFirst'],
            '4':['Gérer les matchs','views.view','View','default'],
            '5':['Gérer les joueurs du tournoi en cours','views.view','View','default'],
            '6':['Statistiques du tournoi en cours','views.view','View','default'],
            '7':['Revenir au menu principal','views.view','View','default'],
        }
        self.showMenu(thisMenu)

    def displayOthersMenu(self):
        thisMenu = {  # 'id':['texte du menu', 'package.module', 'classe', 'methode']
            '1':['Lister les tournois','views.tournamentView','TournamentView','create'],
            '2':["Lister les rounds d'un tournoi",'views.tournamentView','TournamentView','addPlayers'],
            '3':["Lister les matchs d'un tournoi",'views.roundView','RoundView','createFirst'],
            '4':['Revenir au menu principal','views.view','View','default'],
        }
        self.showMenu(thisMenu)

    def create(self):
        print("Nom du tournoi ?")
        name = input()
        print("Lieu du tournoi ?")
        location = input()
        print("Date de début ?")
        startingDate = str(input())
        print("Date de fin ?")
        endingDate = str(input())
        print("Nombre de Rounds ? (3 par défaut) ")
        roundQty = int(input())
        print("Type de tournoi ? (bullet, blitz, coup rapide)")
        type = input()
        print("Description ?")
        description = input()

        createTournamentMethod = self.myRouter.go('controllers.tournamentController','TournamentController','create')
        if (createTournamentMethod(name, location, startingDate, endingDate, roundQty, type, description)):
            self.myRouter.go('views.playersTournamentView','PlayersTournamentView','add')()
        else:
            print('Problème à la saisie des données')

    def displayAll(self):
        for tourney in self.TournamentManager.getAll():
            print(f"{tourney.getId()} : {tourney.getName()}")

    def displayAllRoundsFromCurrentTournament(self, id):
        print(f"Tournoi n° {id} !")
        if (self.RoundManager.getAllFromCurrentTournament(id)):
            for round in self.RoundManager.getAllFromCurrentTournament(id):
                print(f"{round.getId()} : {round.getName()}")
        else:
            print("Créez d'abord un nouveau Round pour ce tournoi !")
            self.myRouter.go('views.roundView','RoundView','create')()

    def selectCurrentTournament(self):
        self.displayAll()
        print("Indiquez le numéro du Tournoi")
        return int(input())

    def selectCurrentRound(self):
        tournamentId = self.selectCurrentTournament()
        self.displayAllRoundsFromCurrentTournament(tournamentId)
        print("Indiquez le numéro du Round")
        return int(input())


        #capturer les input pour appeler tournamentController.createNewTournament() avec :
        #name
        #location
        #startingDate
        #endingDate
        #roundQty
        #type
        #description        

    def display():
        print("display")
        #lister les tournois
        #capturer les input pour appeler tournamentController.createNewTournament() avec :
        #name
        #location
        #startingDate
        #endingDate
        #roundQty
        #type
        #description
