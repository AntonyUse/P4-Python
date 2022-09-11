#!/usr/bin/python

from views.view import View

class PlayerView(View):
    def __init__(self):
        super().__init__()

    def playersMenu(self):
        print('Menu Joueurs')

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
