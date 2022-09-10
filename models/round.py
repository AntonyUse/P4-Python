#!/usr/bin/python

from .object import Object

class Round(Object):  # Round Class
    __slots__ = ['tournament_id', 'name', 'startingDate', 'startingTime', 'endingDate', 'endingTime',]
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

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getStartingDate(self):
        return self.startingDate
    
    def setStartingDate(self, startingDate):
        self.startingDate = startingDate

    def getStartingTime(self):
        return self.startingTime
    
    def setStartingTime(self, startingTime):
        self.startingTime = startingTime

    def getEndingDate(self):
        return self.endingDate
    
    def setEndingDate(self, endingDate):
        self.endingDate = endingDate

    def getEndingTime(self):
        return self.endingTime
    
    def setEndingTime(self, endingTime):
        self.endingTime = endingTime
