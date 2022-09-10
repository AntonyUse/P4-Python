#!/usr/bin/python

from models import db, tournament, round, game, player
import numpy as np

# from views import *

# if __name__ == "__main__":

tournoi = tournament.New('tournaments.csv',['id','name', 'location', 'startingDate', 'endingDate', 'roundQty', 'type', 'description'])
rounds = round.New('rounds.csv',['id','tournament_id','name', 'roundStartingDate', 'roundStartingTime'])
games = game.New('games.csv',['id','round_id','whitePlayerId', 'whitePlayerScore', 'blackPlayerId', 'blackPlayerScore'])
players = player.New('players.csv', ['id', 'name', 'firstname', 'birthdate', 'gender', 'level'])

tournoi.load('tournoi du jeudi', '02/09/2022', '02/09/2022')
players.load()

# generate 1st Round of a tourney
def createGamesOfFirstRound(tournoiId, roundName, players):
    rounds.load(tournoiId, roundName)
    list = np.array_split(sorted(players.list, key=lambda i: i['level'], reverse=True), 2)
    i = 0
    gamesOfFirstRound = []
    for player in list[0]:
        gamesOfFirstRound.append({
            'round_id':rounds.id,
            'whitePlayerId':player['id'],
            'whitePlayerScore':'',
            'blackPlayerId':list[1][i]['id'],
            'blackPlayerScore':''
            })
        i += 1
    games.create(gamesOfFirstRound)

def createGamesOfRound(tournoiId, roundName, players):
    rounds.load(tournoiId, roundName)
    list = np.array_split(sorted(players.list, key=lambda i: i['level'], reverse=True), 2)
    i = 0
    gamesOfRound = []
    for player in list[0]:
        gamesOfRound.append({
            'round_id':rounds.id,
            'whitePlayerId':player['id'],
            'whitePlayerScore':'',
            'blackPlayerId':list[1][i]['id'],
            'blackPlayerScore':''
            })
        i += 1
    games.create(gamesOfRound)

def SetRoundScore(tournoiId, roundName, whitePlayerId, blackPlayerId, winnerId):
    rounds.load(tournoiId, roundName)
    games.load(rounds.id, whitePlayerId, blackPlayerId)
    print(games.whitePlayerId)
    if(winnerId == whitePlayerId):
        games.whitePlayerScore = 1
        games.blackPlayerScore = 0
    elif(winnerId == blackPlayerId):
        games.whitePlayerScore = 0
        games.blackPlayerScore = 1
    else:
        games.whitePlayerScore = float(0.5)
        games.blackPlayerScore = float(0.5)

    games.edit({'id':games.id, 'round_id':rounds.id, 'whitePlayerId':games.whitePlayerId, 'whitePlayerScore':games.whitePlayerScore, 'blackPlayerId':games.blackPlayerId, 'blackPlayerScore':games.blackPlayerScore})

#print(rounds)
#createGamesOfFirstRound(tournoi.id, 'Round 1', players)

#SetRoundScore(tournoi.id, 'Round 1', 11,15,11)