from ghost import Ghost


class Pinky(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y)

    def nextPos(self, state):
        return self.prevPos, self.pos
        