#!/usr/bin/python

import db

class New(db.New):  # Player Class
    def load(self):
        playersList = self.read()
        for player in playersList:
            self.id = player['id']
            self.name = player['name']
            self.firsname = player['firstname']
            self.birthDate = player['birthdate']
            self.gender = player['gender']
            self.level = player['level']
            return True
