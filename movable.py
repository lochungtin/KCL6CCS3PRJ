from constants import *
from displayable import Displayable


class Movable(Displayable):
    def __init__(self, pos, rep):
        super().__init__(pos, rep)
        
        self.prevPos = pos
        self.moved = False

    def isValidPos(self, pos):
        return pos[1] > -1 and pos[1] < BOARD.col and pos[0] > -1 and pos[0] < BOARD.row

    def getDisplayDelta(self):
        if self.moved:
            row, col = self.pos
            pRow, pCol = self.prevPos

            return (col - pCol) * DIM.JUMP, (row - pRow) * DIM.JUMP

        return 0, 0

    def nextPos(self, state):
        return self.prevPos, self.pos
