#!/usr/bin/python

import db

class New(db.New):  # Game Class
    def load(self, round_id):
        gamesList = self.read()
        for game in gamesList:
            if (round_id == game['round_id']):
                self.id = game['id']
                self.whitePlayerRef = game['whitePlayerRef']
                self.whitePlayerScore = game['whitePlayerScore']
                self.blackPlayerRef = game['blackPlayerRef']
                self.blackPlayerScore = game['blackPlayerScore']
                return True
            else:
                return False
