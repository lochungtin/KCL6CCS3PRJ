from data import *
from ghost import Ghost


class Clyde(Ghost):
    def __init__(self, pos):
        super().__init__(pos, REP.CLYDE)
