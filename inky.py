from data import *
from ghost import Ghost


class Inky(Ghost):
    def __init__(self, pos):
        super().__init__(pos, REP.INKY)
