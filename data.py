from typing import List, Tuple


# dimension values of the board
class BOARD:
    row: int = 31
    col: int = 27


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
    TOTAL_PELLET_COUNT: int = 238
    TOTAL_PWRPLT_COUNT: int = 4

    CRUISE_ELROY_TRIGGER: int = 20

    # ghost mode and step counter
    TOTAL_STEP_COUNT: int = 840

    GHOST_EXIT_INTERVAL: int = 30

    GHOST_FRIGHTENED_SPEED_REDUCTION_RATE: int = 3
    GHOST_FRIGHTENED_STEP_COUNT: int = 80
    GHOST_MODE_SCHEDULE: List[Tuple[int, int]] = [
        (GHOST_MODE.SCATTER, 770),
        (GHOST_MODE.CHASE, 570),
        (GHOST_MODE.SCATTER, 500),
        (GHOST_MODE.CHASE, 300),
        (GHOST_MODE.SCATTER, 250),
        (GHOST_MODE.CHASE, 50),
        (GHOST_MODE.SCATTER, 0),
        (GHOST_MODE.CHASE, -1),
    ]

# pixel values of components
class DIM:
    # canvas pixel count
    GBL_H: int = 925
    GBL_W: int = 805

    # grid cell and gap size
    JUMP: int = 30
    CELL: int = 25
    GAP: int = 5

    # padding for objects
    PAD_PELLET: int = 9
    PAD_PWRPLT: int = 5
    PAD_DOOR: int = 8


# directions of movement
class DIR:
    UP: int = 0
    DW: int = 1
    LF: int = 2
    RT: int = 3

    def getOpposite(dir: int) -> int:
        if dir == DIR.UP:
            return DIR.DW
        elif dir == DIR.DW:
            return DIR.UP
        elif dir == DIR.LF:
            return DIR.RT
        return DIR.LF


# initial position of displayables
from utils.coordinate import CPair
class POS:
    # initial pacman location
    PACMAN: CPair = CPair(23, 13)

    # initial ghost locations
    BLINKY: CPair = CPair(11, 13)
    INKY: CPair = CPair(14, 11)
    CLYDE: CPair = CPair(14, 15)
    PINKY: CPair = CPair(14, 13)


    # special locations
    # ghost house reset location
    GHOST_HOUSE_CENTER: CPair = CPair(14, 13)

    # scatter mode target corners
    BLINKY_CORNER: CPair = CPair(1, 25)
    INKY_CORNER: CPair = CPair(29, 25)
    CLYDE_CORNER: CPair = CPair(29, 1)
    PINKY_CORNER: CPair = CPair(1, 1)

    # loop triggers
    LEFT_LOOP_TRIGGER: CPair = CPair(14, -1)
    LEFT_LOOP: CPair = CPair(14, 0)

    RIGHT_LOOP_TRIGGER: CPair = CPair(14, 27)
    RIGHT_LOOP: CPair = CPair(14, 26)

    # "no go up" zones
    GHOST_NO_UP_1: CPair = CPair(11, 12)
    GHOST_NO_UP_2: CPair = CPair(11, 14)
    GHOST_NO_UP_3: CPair = CPair(23, 12)
    GHOST_NO_UP_4: CPair = CPair(23, 14)

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

    # classic colors
    # COLOR_MAP: dict[int, str] = {
    #     0: "#1e1e1e",
    #     1: "#3a60de",
    #     2: "#f255c8",
    #     3: "#f1f2da",
    #     4: "#f1f2da",
    #     5: "#e8d22a",
    #     6: "#e62C4e",
    #     7: "#27ebf2",
    #     8: "#f255c8",
    #     9: "#ff9f29",
    #     10: "#1330c2",
    #     11: "#505050",
    # }

    # my colors
    COLOR_MAP: dict[int, str] = {
        0: "#1e1e1e",
        1: "#292929",
        2: "#292929",
        3: "#52756a",
        4: "#8ebdae",
        5: "#6bf2c7",
        6: "#e36685",
        7: "#71c8e3",
        8: "#e771eb",
        9: "#edb974",
        10: "#c0c0c0",
        11: "#505050",
    }

    # board pattern for path and walls
    BOARD: List[List[int]] = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 2, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # board pattern for pellets and power pellets
    PELLET_BOARD: List[List[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 4, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 4, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 4, 0],
        [0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
