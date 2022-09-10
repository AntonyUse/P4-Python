#!/usr/bin/python

from models import db

# player = player.New('players.csv', ['id', 'name', 'firstname', 'birthdate', 'gender', 'level'])
# player1 = {'name':'Courtin', 'firstname':'Alex', 'birthdate':'', 'gender':'F', 'level':'1'}
# player2 = {'name':'Use', 'firstname':'Elric', 'birthdate':'', 'gender':'M', 'level':'3'}
# player3 = {'name':'Use', 'firstname':'Kenji', 'birthdate':'', 'gender':'M', 'level':'2'}
# player4 = {'name':'Use', 'firstname':'Anto', 'birthdate':'', 'gender':'M', 'level':'5'}
# player5 = {'name':'DanleQ', 'firstname':'Robert', 'birthdate':'', 'gender':'M', 'level':'12'}
# player6 = {'name':'Canap', 'firstname':'Jenna', 'birthdate':'', 'gender':'F', 'level':'0'}
# player7 = {'name':'Yaki', 'firstname':'Terry', 'birthdate':'', 'gender':'M', 'level':'8'}
# player8 = {'name':'Canette', 'firstname':'John', 'birthdate':'', 'gender':'M', 'level':'44'}
# player9 = {'name':'Hadi', 'firstname':'Jack', 'birthdate':'', 'gender':'M', 'level':'37'}
# player10 = {'name':'Terre', 'firstname':'Jean', 'birthdate':'', 'gender':'F', 'level':'28'}
# player11 = {'name':'Lane', 'firstname':'Pedro', 'birthdate':'', 'gender':'M', 'level':'14'}
# player12 = {'name':'Stochat', 'firstname':'Harry', 'birthdate':'', 'gender':'M', 'level':'84'}
# player13 = {'name':'Bis', 'firstname':'Pedro', 'birthdate':'', 'gender':'M', 'level':'54'}
# player14 = {'name':'Dent', 'firstname':'Harvey', 'birthdate':'', 'gender':'M', 'level':'65'}
# player15 = {'name':'Corne', 'firstname':'Sally', 'birthdate':'', 'gender':'F', 'level':'6'}
# player16 = {'name':'Logan', 'firstname':'Renaud', 'birthdate':'', 'gender':'M', 'level':'11'}

# player.create([
#    player1,
#    player2,
#    player3,
#    player4,
#    player5,
#    player6,
#    player7,
#    player8,
#    player9,
#    player10,
#    player11,
#    player12,
#    player13,
#    player14,
#    player15,
#    player16])

class New(db.New):  # Player Class
    def load(self):
        self.list = []
        playersList = self.read()
        for player in playersList:
            self.list.append({
                'id':int(player['id']),
                'name':player['name'],
                'firsname':player['firstname'],
                'birthDate':player['birthdate'],
                'gender':player['gender'],
                'level':int(player['level'])
                })

        return True
