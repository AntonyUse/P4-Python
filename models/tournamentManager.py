#!/usr/bin/python

from .manager import Manager
from .tournament import Tournament

class TournamentManager(Manager):
# CRUD
    def create(self,tournamentObj):
        dict = {
            'name':tournamentObj.getName(),
            'location':tournamentObj.getLocation(),
            'startingDate':tournamentObj.getStartingDate(),
            'endingDate':tournamentObj.getEndingDate(),
            'roundQty':tournamentObj.getRoundQty(),
            'type':tournamentObj.getType(),
            'description':tournamentObj.getDescription(),
            }
        return super().create(dict)

    def getOne(self, id):
        row = super().getOne(id)
        tourney = Tournament(**row)
        tourney.setId(row.doc_id)
        return tourney

    def getLast(self):
        row = super().getLast()
        tourney = Tournament(**row)
        tourney.setId(row.doc_id)
        return tourney

    def getAll(self):
        rows = super().getAll()
        tournamentsList = []
        for row in rows:
            tour = Tournament(**row)
            tour.setId(row.doc_id)
            tournamentsList.append(tour)
        return tournamentsList

    def update(self,tournamentObj):
        return super().update({
            'name':tournamentObj.getName(),
            'location':tournamentObj.getLocation(),
            'startingDate':tournamentObj.getStartingDate(),
            'endingDate':tournamentObj.getEndingDate(),
            'roundQty':tournamentObj.getRoundQty(),
            'type':tournamentObj.getType(),
            'description':tournamentObj.getDescription()
            }, tournamentObj.getId())

    def delete(self,id):
        return super().delete(id)
