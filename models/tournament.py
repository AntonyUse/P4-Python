#!/usr/bin/python

from .object import Object

class Tournament(Object):  # Tournament Class
    __slots__ = ['name', 'location', 'startingDate', 'endingDate', 'roundQty', 'type', 'description']
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.doc_id = ''

# getters and setters
    def getId(self):
        return self.doc_id
    
    def setId(self, id):
        self.doc_id = id

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getLocation(self):
        return self.location
    
    def setLocation(self, location):
        self.location = location

    def getStartingDate(self):
        return self.startingDate
    
    def setStartingDate(self, startingDate):
        self.startingDate = startingDate

    def getEndingDate(self):
        return self.endingDate
    
    def setEndingDate(self, endingDate):
        self.endingDate = endingDate

    def getRoundQty(self):
        return self.roundQty
    
    def setRoundQty(self, roundQty):
        self.roundQty = roundQty

    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type

    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description
