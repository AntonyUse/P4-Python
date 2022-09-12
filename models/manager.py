#!/usr/bin/python

from .db import Db
from tinydb import Query

class Manager(Db):
    __slots__ = 'dbTable'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.table = self.db.table(self.dbTable)
    
    def create(self,dict):
        return self.table.insert(dict)

    def getOne(self, id):
        return self.table.get(doc_id=id)

    def getAll(self):
        return self.table.all()

    def getLast(self):
        return self.table.all()[-1]

    def getAllFromKey(self,key, value):
        return self.table.search(Query()[key] == value)

    def update(self, dict, id):
        return self.table.update(dict, doc_ids=[int(id)])

    def delete(self,id):
        return self.table.remove(doc_ids=[int(id)])
