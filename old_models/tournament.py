#!/usr/bin/python

from models import db

# tournoi = tournament.New('tournaments.csv',['id','name', 'location', 'startingDate', 'endingDate', 'roundQty', 'type', 'description'])
# tournoi.create([{'name':'tournoi du jeudi', 'location':'ici', 'startingDate':'02/09/2022', 'endingDate':'02/09/2022',  'roundQty':3, 'type':'bullet', 'description':"un essai"}])

class New(db.New):  # Tournament Class
    def load(self, name, startingDate, endingDate):
        tournamentsList = self.read()
        for tourney in tournamentsList:
            if (name == tourney['name'] and
                    startingDate == tourney['startingDate'] and
                    endingDate == tourney['endingDate']):
                self.id = int(tourney['id'])
                self.name = tourney['name']
                self.location = tourney['location']
                self.startingDate = tourney['startingDate']
                self.endingDate = tourney['endingDate']
                self.roundQty = int(tourney['roundQty'])
                self.type = tourney['type']  # bullet/blitz/coup rapide
                self.description = tourney['description']
                return True
            else:
                return False

    def addRound(self, roundRef):
        self.roundsRefsList.append(roundRef)

    def getStandings(self):
        return

    def getPlayersReport(self, sorting):
        return

    def getTournamentsList(self):
        return

    def getTournamentRounds(self):
        return self.rounds

    def getTournamentGames(self):
        return
