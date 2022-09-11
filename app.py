#!/usr/bin/python

from views.view import View

homeMenu = {  # 'id':['texte du menu', 'package.module', 'classe', 'methode']
    '1':['Créer un nouveau tournoi','views.tournamentView','TournamentView','create'],
    '2':['Gérer votre tournoi en cours',''],
    '3':['Gérer les autres tournois',''],
    '4':['Sortie','exit'],
}

myView = View()
myView.showMenu(homeMenu)