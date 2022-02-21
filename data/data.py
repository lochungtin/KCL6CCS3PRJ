from typing import List, Tuple

from data.config import BOARD

# ghost ai modes
class GHOST_MODE:
    CHASE: int = 0
    SCATTER: int = 1
    FRIGHTENED: int = 2
    DEAD: int = 3

    # blinky
    CRUISE_ELROY: int = 4


# game related data constants
class DATA:
    # number of pellets
    TOTAL_PELLET_COUNT: int = 68
    TOTAL_PWRPLT_COUNT: int = 2

    CRUISE_ELROY_TRIGGER: int = 12

    # ghost mode and step counter
    TOTAL_STEP_COUNT: int = 84

    GHOST_EXIT_INTERVAL: int = 3

    GHOST_FRIGHTENED_SPEED_REDUCTION_RATE: int = 3
    GHOST_FRIGHTENED_STEP_COUNT: int = 7
    GHOST_MODE_SCHEDULE: List[Tuple[int, int]] = [
        (GHOST_MODE.SCATTER, 77),
        (GHOST_MODE.CHASE, 57),
        (GHOST_MODE.SCATTER, 50),
        (GHOST_MODE.CHASE, 30),
        (GHOST_MODE.SCATTER, 25),
        (GHOST_MODE.CHASE, 5),
        (GHOST_MODE.SCATTER, 0),
        (GHOST_MODE.CHASE, -1),
    ]


# pixel values of components
class DIM:
    # grid cell and gap size
    JUMP: int = 30
    CELL: int = 25
    GAP: int = 5

    # canvas pixel count
    GBL_H: int = BOARD.ROW * JUMP - GAP
    GBL_W: int = BOARD.COL * JUMP - GAP

    # padding for objects
    PAD_PELLET: int = 9
    PAD_PWRPLT: int = 5
    PAD_DOOR: int = 8


# state representations
class REP:
    BG: int = 0
    EMPTY: int = 0
    WALL: int = 1
    DOOR: int = 2
    PELLET: int = 3
    PWRPLT: int = 4
    PACMAN: int = 5
    BLINKY: int = 6
    INKY: int = 7
    PINKY: int = 8
    CLYDE: int = 9
    FRIGHTENED: int = 10
    DEAD: int = 11

    def isWall(rep: int) -> bool:
        return rep == 1 or rep == 2

    def isPellet(rep: int) -> bool:
        return rep == 3 or rep == 4

    def isGhost(rep: int) -> bool:
        return rep > 5 and rep < 10
