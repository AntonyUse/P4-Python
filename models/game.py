#!/usr/bin/python

from .object import Object

class Game(Object):  # Game Class
    __slots__ = ['tournament_id', 'round_id', 'whitePlayerId', 'whitePlayerScore', 'blackPlayerId', 'blackPlayerScore']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doc_id = ''

# getters and setters
    def getId(self):
        return self.doc_id
    
    def setId(self, id):
        self.doc_id = id

    def getTournamentId(self):
        return self.tournament_id
    
    def setTournamentId(self, tournament_id):
        self.tournament_id = tournament_id

    def getRoundId(self):
        return self.round_id
    
    def setRoundId(self, round_id):
        self.round_id = round_id

    def getWhitePlayerId(self):
        return self.whitePlayerId
    
    def setWhitePlayerId(self, whitePlayerId):
        self.whitePlayerId = whitePlayerId

    def getWhitePlayerScore(self):
        return self.whitePlayerScore
    
    def setWhitePlayerScore(self, whitePlayerScore):
        self.whitePlayerScore = whitePlayerScore

    def getBlackPlayerId(self):
        return self.blackPlayerId
    
    def setBlackPlayerId(self, blackPlayerId):
        self.blackPlayerId = blackPlayerId

    def getBlackPlayerScore(self):
        return self.blackPlayerScore
    
    def setBlackPlayerScore(self, blackPlayerScore):
        self.blackPlayerScore = blackPlayerScore
