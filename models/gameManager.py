#!/usr/bin/python

from .manager import Manager
from .game import Game

class GameManager(Manager):
# CRUD
    def create(self,gameObj):
        dict = {
            'tournament_id':gameObj.getTournamentId(),
            'round_id':gameObj.getRoundId(),
            'whitePlayerId':gameObj.getWhitePlayerId(),
            'whitePlayerScore':gameObj.getWhitePlayerScore(),
            'blackPlayerId':gameObj.getBlackPlayerId(),
            'blackPlayerScore':gameObj.getBlackPlayerScore(),
        }
        return super().create(dict)

    def getOne(self, id):
        row = super().getOne(id)
        gameey = Game(**row)
        gameey.setId(row.doc_id)
        return gameey

    def getLast(self):
        row = super().getLast()
        gameey = Game(**row)
        gameey.setId(row.doc_id)
        return gameey

    def getAll(self):
        rows = super().getAll()
        gamesList = []
        for row in rows:
            tour = Game(**row)
            tour.setId(row.doc_id)
            gamesList.append(tour)
        return gamesList

    def update(self,gameObj):
        return super().update({
            'tournament_id':gameObj.getTournamentId(),
            'round_id':gameObj.getRoundId(),
            'whitePlayerId':gameObj.getWhitePlayerId(),
            'whitePlayerScore':gameObj.getWhitePlayerScore(),
            'blackPlayerId':gameObj.getBlackPlayerId(),
            'blackPlayerScore':gameObj.getBlackPlayerScore(),
            }, gameObj.getId())

    def delete(self,id):
        return super().delete(id)
