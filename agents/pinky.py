from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.game import Game

from agents.base.ghost import ClassicGhostAgent, StaticGhostAgent
from data.config import POS
from data.data import GHOST_MODE, REP
from utils.coordinate import CPair
from utils.direction import DIR


# original agent for pinky
class PinkyClassicAgent(ClassicGhostAgent):
    def __init__(self) -> None:
        super().__init__(POS.PINKY, REP.PINKY, 0)

    # get target tile of ghost
    def getTargetTile(self, game: "Game") -> CPair:
        # scatter mode (head to corner)
        if self.mode == GHOST_MODE.SCATTER:
            return POS.PINKY_CORNER

        # chase mode
        targetTile: CPair = game.pacman.pos
        for _ in range(2):
            targetTile = targetTile.move(game.pacman.direction)

        # replicate target tile bug in classic pacman
        if game.pacman.direction == DIR.UP:
            for _ in range(2):
                targetTile = targetTile.move(DIR.LF)

        return targetTile


# hyperaggressive agent for pinky
class PinkyClassicAggrAgent(ClassicGhostAgent):
    def __init__(self) -> None:
        super().__init__(POS.PINKY, REP.PINKY, 0)

    # get target tile of ghost
    def getTargetTile(self, game: "Game") -> CPair:
        # chase mode
        targetTile: CPair = game.pacman.pos
        for _ in range(2):
            targetTile = targetTile.move(game.pacman.direction)

        # replicate target tile bug in classic pacman
        if game.pacman.direction == DIR.UP:
            for _ in range(2):
                targetTile = targetTile.move(DIR.LF)

        return targetTile


# static agent for pinky
class PinkyStaticAgent(StaticGhostAgent):
    def __init__(self) -> None:
        StaticGhostAgent.__init__(self, POS.PINKY, REP.PINKY)
