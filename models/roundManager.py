#!/usr/bin/python

from .manager import Manager
from .round import Round

class RoundManager(Manager):
# CRUD
    def create(self,roundObj):
        dict = {
            'tournament_id':roundObj.getTournamentId(),
            'name':roundObj.getName(),
            'startingDate':roundObj.getStartingDate(),
            'startingTime':roundObj.getStartingTime(),
            'endingDate':roundObj.getEndingDate(),
            'endingTime':roundObj.getEndingTime(),
        }
        return super().create(dict)

    def getOne(self, id):
        row = super().getOne(id)
        roundey = Round(**row)
        roundey.setId(row.doc_id)
        return roundey

    def getLast(self):
        row = super().getLast()
        roundey = Round(**row)
        roundey.setId(row.doc_id)
        return roundey

    def getAll(self):
        rows = super().getAll()
        roundsList = []
        for row in rows:
            tour = Round(**row)
            tour.setId(row.doc_id)
            roundsList.append(tour)
        return roundsList

    def getAllFromCurrentTournament(self, tournamentId):
        rows = super().getAllFromKey('tournament_id', tournamentId)
        roundsList = []
        for row in rows:
            tour = Round(**row)
            tour.setId(row.doc_id)
            roundsList.append(tour)
        return roundsList

    def update(self,roundObj):
        return super().update({
            'tournament_id':roundObj.getTournamentId(),
            'name':roundObj.getName(),
            'startingDate':roundObj.getStartingDate(),
            'startingTime':roundObj.getStartingTime(),
            'endingDate':roundObj.getEndingDate(),
            'endingTime':roundObj.getEndingTime(),
            }, roundObj.getId())

    def delete(self,id):
        return super().delete(id)
