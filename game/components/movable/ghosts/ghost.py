from typing import List, Tuple
import random

from data import DATA, DIR, GHOST_MODE, POS, REP
from game.components.movable.movable import Movable
from game.components.movable.pacman import Pacman
from game.utils.path import Path
from game.utils.pathfinder import PathFinder
from utils.coordinate import CPair


class Ghost(Movable):
    def __init__(self, pos: CPair, repId: int, initWait: int, pf: PathFinder) -> None:
        super().__init__(pos, repId)

        self.mode: int = GHOST_MODE.SCATTER
        self.isDead: bool = False
        self.isFrightened: bool = False
        self.speedReducer: int = 2

        self.pathfinder: PathFinder = pf
        self.path: Path = Path()
        self.prevPath: Path = Path()

        self.initWait: int = initWait

    # modified version of getNeighbours to accomodate for "no go up" zones
    def getNeighbours(self, state: List[List[int]]) -> List[CPair]:
        rt: List[CPair] = []

        for index, pos in enumerate(self.pos.getNeighbours()):
            if (
                (
                    pos == POS.GHOST_NO_UP_1
                    or pos == POS.GHOST_NO_UP_2
                    or pos == POS.GHOST_NO_UP_3
                    or pos == POS.GHOST_NO_UP_4
                )
                and index == 0
                or REP.isWall(state[pos.row][pos.col])
                or DIR.getOpposite(self.direction) == index
            ):
                continue

            rt.append(pos)

        return rt

    # get target tile of ghost
    def getTargetTile(self, pacman: Pacman, blinkyPos: CPair) -> CPair:
        return CPair(1, 1)

    # get next position of ghost
    def getNextPos(
        self, state: List[List[int]], pacman: Pacman, blinkyPos: CPair
    ) -> Tuple[CPair, CPair]:
        # wait at ghost house
        if self.initWait > -1:
            self.initWait -= 1
            return self.pos, self.pos

        # dead and returned to ghost house
        if self.isDead and self.pos == POS.GHOST_HOUSE_CENTER:
            self.isDead = False

        # start random walk if frightened
        if self.isFrightened:
            # update prev pos
            self.prevPos = self.pos

            # reverse direction for first step
            # hold position if reverse is invalid
            if self.speedReducer == DATA.GHOST_FRIGHTENED_SPEED_REDUCTION_RATE:
                newPos = self.pos.move(DIR.getOpposite(self.direction))
                if newPos.isValid() and not REP.isWall(state[newPos.row][newPos.col]):
                    self.pos = newPos

                self.speedReducer = DATA.GHOST_FRIGHTENED_SPEED_REDUCTION_RATE - 1

            # slow down ghost speed (walk every 2 time steps)
            self.speedReducer = (self.speedReducer + 1) % DATA.GHOST_FRIGHTENED_SPEED_REDUCTION_RATE
            if self.speedReducer == 0:
                self.pos = random.choice(self.getNeighbours(state))

        # normal behaviour
        else:
            # get target tile
            # loop mechanic
            targetTile: CPair = self.getTargetTile(pacman, blinkyPos)
            if self.pos == targetTile:
                targetTile = self.prevPos

            # generate path
            self.prevPath = self.path
            self.path = self.pathfinder.start(self.pos, targetTile, self.direction)

            self.prevPos = self.pos
            if len(self.path.path) > 0:
                self.pos = self.path.path[0]

        # update direction of travel
        if self.pos != self.prevPos:
            self.direction = self.pos.relate(self.prevPos)

        return self.pos, self.prevPos
