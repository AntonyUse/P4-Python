#!/usr/bin/python

from models import object
from dateutil.parser import parse

class Controller(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def is_date(string, fuzzy=False):
        try: 
            parse(string, fuzzy=fuzzy)
            return True

        except ValueError:
            return False