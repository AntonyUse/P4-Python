#!/usr/bin/python

from .controller import Controller
from models.player import Player
from models.playerManager import PlayerManager

class PlayerController(Controller):
    def __init__(self):
        super().__init__()
        self.playerManager = PlayerManager(file='db.json', dbTable='players')

    # from Menu 1.1 to Menu 1.2
    def create(self, name, firstname, birthdate, gender, level):
        genderList = ['M', 'F']
        if (
            name and 
            firstname and 
            birthdate and 
            genderList.count(gender) > 0 and 
            isinstance(level, int)
            ):
            print('toto')
            try:
                self.player = Player(name=name, firstname=firstname, birthdate=birthdate, gender=gender, level=level)
                self.playerManager.create(self.player)
                return True
            except ValueError:
                return "Impossible de créer le joueur"
        else:
            print('titi', name, firstname, birthdate, gender, level)
            return False

    def update(self, id, name, firstname, birthdate, gender, level):
        try:
            self.player = self.playerManager.getOne(id)
            print(self.player.firstname)
            if (name):
                self.player.setName(name)

            if (firstname):
                self.player.setFirstname(firstname)

            if (birthdate):
                self.player.setBirthdate(birthdate)

            if (gender):
                self.player.setGender(gender)

            if (level):
                self.player.setLvel(level)

            self.playerManager.update(self.player)
            return True
        except ValueError:
            return "Impossible de modifier le joueur"

    def delete(self, id):
        try:
            self.playerManager.delete(id)
            return True
        except ValueError:
            return "Impossible de supprimer le joueur"
