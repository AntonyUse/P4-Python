#!/usr/bin/python

from .manager import Manager
from .player import Player

class PlayerManager(Manager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
# CRUD
    def create(self,playerObj):
        dict = {
            'name':playerObj.getName(),
            'firstname':playerObj.getFirstname(),
            'birthdate':playerObj.getBirthdate(),
            'gender':playerObj.getGender(),
            'level':playerObj.getLevel(),
        }
        return super().create(dict)

    def getOne(self, id):
        row = super().getOne(id)
        playerey = Player(**row)
        playerey.setId(row.doc_id)
        return playerey

    def getLast(self):
        row = super().getLast()
        playerey = Player(**row)
        playerey.setId(row.doc_id)
        return playerey

    def getAll(self):
        rows = super().getAll()
        playersList = []
        for row in rows:
            tour = Player(**row)
            tour.setId(row.doc_id)
            playersList.append(tour)
        return playersList

    def update(self,playerObj):
        return super().update({
            'name':playerObj.getName(),
            'firstname':playerObj.getFirstname(),
            'birthdate':playerObj.getBirthdate(),
            'gender':playerObj.getGender(),
            'level':playerObj.getLevel(),
            }, playerObj.getId())

    def delete(self,id):
        return super().delete(id)
