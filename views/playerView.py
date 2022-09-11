#!/usr/bin/python

from xml.dom.pulldom import END_ELEMENT
import router

class PlayerView():
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
        roundQty = input()
        print("Type de tournoi ? (bullet, blitz, coup rapide)")
        type = input()
        print("Description ?")
        description = input()

        myRouter = router.Router
        myMethod = myRouter.go('controllers.tournamentController','TournamentController','create')
        myMethod(name, location, startingDate, endingDate, roundQty, type, description)

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
