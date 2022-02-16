from random import randint
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from game.game import Game

from agents.base import Agent, DirectionAgent
from ai.predictable import Predictable
from data.data import BOARD, DIR, GHOST_MODE, POS, REP
from utils.coordinate import CPair


# pacman base agent
class PacmanBaseAgent(Agent):
    def __init__(self) -> None:
        super().__init__(POS.PACMAN, REP.PACMAN)


# playable keyboard agent for pacman
class PlayableAgent(DirectionAgent):
    def __init__(self) -> None:
        super().__init__(POS.PACMAN, REP.PACMAN)


# # neat agent for pacman
# class NEATAgent(PacmanBaseAgent, IntelligentBase):
#     def __init__(self, predictable: Predictable) -> None:
#         IntelligentBase.__init__(self, POS.PACMAN, REP.PACMAN, predictable)

#     def locComp(self, pov: CPair, loc: CPair) -> List[int]:
#         return [
#             int(pov.row > loc.row),  # should move up
#             int(pov.row < loc.row),  # should move down
#             int(pov.col > loc.col),  # should move left
#             int(pov.col < loc.col),  # should move right
#         ]

#     def processState(self, game: "Game") -> List[int]:
#         input: List[int] = []

#         pacPos: CPair = game.pacman.pos
#         for newPos in pacPos.getNeighbours(True):
#             valid: bool = False
#             if hasattr(newPos, "row"):
#                 valid = not REP.isWall(game.state[newPos.row][newPos.col])

#             input.append(int(valid))

#         pltDist: int = 2 * BOARD.row
#         pwrDist: int = 2 * BOARD.row

#         pltPos: CPair = pacPos
#         pwrPos: CPair = pacPos

#         for r in range(BOARD.row):
#             for c in range(BOARD.col):
#                 cell = game.state[r][c]
#                 manDist: int = abs(pacPos.row - r) + abs(pacPos.col - c)

#                 if cell == REP.PELLET and manDist < pltDist:
#                     pltDist = manDist
#                     pltPos = CPair(r, c)

#                 elif cell == REP.PWRPLT and manDist < pwrDist:
#                     pwrDist = manDist
#                     pwrPos = CPair(r, c)

#         if pltPos != pacPos:
#             pltPos = game.pathfinder.start(pacPos, pltPos, -1).path[0]

#         if pwrPos != pacPos:
#             pwrPos = game.pathfinder.start(pacPos, pwrPos, -1).path[0]

#         input += self.locComp(pacPos, pltPos)
#         input += self.locComp(pacPos, pwrPos)

#         if hasattr(game, "ghosts"):
#             for ghost in game.ghosts:
#                 input += self.locComp(pacPos, ghost.pos)
#                 input.append(abs(pacPos.row - ghost.pos.row) + abs(pacPos.col - ghost.pos.col))
#                 input.append(int(ghost.isFrightened))

#             input.append(int(game.inky.mode == GHOST_MODE.CHASE))
#         else:
#             for _ in range(25):
#                 input.append(0)

#         return input
