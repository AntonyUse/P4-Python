#!/usr/bin/python

from .object import Object

class Player(Object):  # Player Class
    __slots__ = ['name', 'firstname', 'birthdate', 'gender', 'level']
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

    def getFirstname(self):
        return self.firstname
    
    def setFirstame(self, firstname):
        self.firstname = firstname

    def getBirthdate(self):
        return self.birthdate
    
    def setBirthdate(self, birthdate):
        self.birthdate = birthdate

    def getGender(self):
        return self.gender
    
    def setGender(self, gender):
        self.gender = gender

    def getLevel(self):
        return self.level
    
    def setLevel(self, level):
        self.level = level
