#!/usr/bin/python

from views.view import View

homeMenu = {
    '1':['Créer un nouveau tournoi','controllers.tournamentController','TournamentController','createNewTournament'],
    '2':['Gérer votre tournoi en cours',''],
    '3':['Gérer les autres tournois',''],
    '4':['Sortie','exit'],
}

myView = View()
myView.showMenu(homeMenu)