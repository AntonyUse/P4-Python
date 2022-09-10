#!/usr/bin/python

from models import db

# theRound = round.New('rounds.csv',['id','tournament_id','name', 'roundStartingDate', 'roundStartingTime'])
# theRound.create([{'tournament_id':tournoi.id,'name':'1st Round', 'roundStartingDate':'02/09/2022', 'roundStartingTime':'12:25'}])
class New(db.New):  # Round Class
    def load(self, tournament_id, name):
        roundsList = self.read()
        for round in roundsList:
            if (round['name'] == name and int(round['tournament_id']) == int(tournament_id)): 
                print(tournament_id)
                self.id = int(round['id'])
                self.name = round['name']
                self.tournament_id = int(round['tournament_id'])
                self.roundStartingDate = round['roundStartingDate']
                self.roundStartingTime = round['roundStartingTime']
                return True
            else:
                return False

    def close(self, roundEndingDate, roundEndingTime):
        self.roundEndingDate = roundEndingDate
        self.roundEndingTime = roundEndingTime
