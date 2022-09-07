#!/usr/bin/python

from models import db, tournament, round, game, player
# from views import *

# if __name__ == "__main__":

player = player.New('players.csv', ['id', 'name', 'firstname', 'birthdate', 'gender', 'level'])
player1 = {'Courtin', 'Alex', 'birthdate', 'F', '1'}
player2 = {'Use', 'Elric', 'birthdate', 'M', '3'}
player3 = {'Use', 'Kenji', 'birthdate', 'M', '2'}
player4 = {'Use', 'Anto', 'birthdate', 'M', '5'}
player5 = {'DanleQ', 'Robert', 'birthdate', 'M', '12'}
player6 = {'Canap', 'Jenna', 'birthdate', 'F', '0'}
player7 = {'Yaki', 'Terry', 'birthdate', 'M', '8'}
player8 = {'Canette', 'John', 'birthdate', 'M', '44'}
player9 = {'Hadi', 'Jack', 'birthdate', 'M', '37'}
player10 = {'Terre', 'Jean', 'birthdate', 'F', '28'}
player11 = {'Lane', 'Pedro', 'birthdate', 'M', '14'}
player12 = {'Stochat', 'Harry', 'birthdate', 'M', '84'}
player13 = {'Bis', 'Pedro', 'birthdate', 'M', '54'}
player14 = {'Dent', 'Harvey', 'birthdate', 'M', '65'}
player15 = {'Corne', 'Sally', 'birthdate', 'F', '6'}
player16 = {'Logan', 'Renaud', 'birthdate', 'M', '11'}

player.create([
    player1,
    player2,
    player3,
    player4,
    player5,
    player6,
    player7,
    player8,
    player9,
    player10,
    player11,
    player12,
    player13,
    player14,
    player15,
    player16])
