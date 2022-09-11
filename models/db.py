#!/usr/bin/python

from .object import Object
from tinydb import TinyDB

class Db(Object):
    __slots__= 'file'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = TinyDB(self.file)
        

    def getDb(self):
        return self.db
    
    def setDb(self, file):
        self.file = file
        self.db = TinyDB(file)
