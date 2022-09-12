#!/usr/bin/python

from .controller import Controller
from models.tournament import Tournament
from models.tournamentManager import TournamentManager

class TournamentController(Controller):
    def __init__(self):
        super().__init__()
        self.tournamentManager = TournamentManager(file='db.json', dbTable='tournaments')

    # from Menu 1.1 to Menu 1.2
    def create(self, name, location, startingDate, endingDate, roundQty, type, description):
        typeList = ['bullet', 'blitz', 'coup rapide']
        if (
            name and 
            location and 
            startingDate and 
            isinstance(roundQty, int) and             
            typeList.count(type) > 0 and 
            description
            ):
            try:
                self.tournament = Tournament(
                    name=name,
                    location=location,
                    startingDate=startingDate,
                    endingDate=endingDate,
                    roundQty=roundQty,
                    type=type,
                    description=description
                    )
                self.tournamentManager.create(self.tournament)
                return True
            except ValueError:
                return "Impossible de créer le tournoi"
        else:
            return False


#list = tourneyManager.getAll()
#for tour in list:
#    print(tour.getId(), tour.getName())

#tourn = tourneyManager.getLast()
#tourn.setName('tournoi du vendredi')
#print(tourn.getName())

#tourneyManager.update(tourn)
#list = tourneyManager.getAll()
#for tour in list:
#    print(tour.getId(), tour.getName())

#tourne = tourneyManager.getOne('3')
#print(tourne.getName(), tourne.getId())

#round1 = tournament.Tournament(tournament_id=3, name='Round 1', startingDate='02/09/2022', startingTime='12:25', endingDate='', endingTime='')
#roundeyManager = roundManager.RoundManager(file='db.json', dbTable='rounds')
#roundeyManager.create(round1)