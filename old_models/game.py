#!/usr/bin/python

from models import db

class New(db.New):  # Game Class
    def load(self, round_id, whitePlayerId, blackPlayerId):
        gamesList = self.read()
        for game in gamesList:
            if (
                int(game['round_id']) == int(round_id) and 
                int(game['whitePlayerId']) == int(whitePlayerId) and 
                int(game['blackPlayerId']) == int(blackPlayerId)):
                
                self.id = game['id']
                self.whitePlayerId = int(game['whitePlayerId'])
                self.whitePlayerScore = game['whitePlayerScore']
                self.blackPlayerId = int(game['blackPlayerId'])
                self.blackPlayerScore = game['blackPlayerScore']
                return True
        
    def getAllGamesOfRound(self, round_id):
        gamesList = self.read()
        gamesOfTheRound = []
        for game in gamesList:
            if (
                int(game['round_id']) == int(round_id)):
                self.id = game['id']
                self.whitePlayerId = int(game['whitePlayerId'])
                self.whitePlayerScore = game['whitePlayerScore']
                self.blackPlayerId = int(game['blackPlayerId'])
                self.blackPlayerScore = game['blackPlayerScore']
                return True

