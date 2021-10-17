from typing import Tuple

from data import DIR, REP
from game.components.movable.movable import Movable
from utils.coordinate import CPair


class Pacman(Movable):
    def __init__(self, pos: CPair) -> None:
        super().__init__(pos, REP.PACMAN)

        self.direction: int = DIR.UP

    def getNextPos(self) -> Tuple[CPair, CPair]:
        return super().getNextPos()
