# dimension values of the board
class BOARD:
    row = 31
    col = 27


# pixel values of components
class DIM:
    GBL_H = 925
    GBL_W = 805

    JUMP = 30
    CELL = 25
    GAP = 5

    PAD_ORB = 9
    PAD_PWRPLT = 5
    PAD_DOOR = 8


# directions of movement
class DIR:
    UP = 0
    DW = 1
    RT = 2
    LF = 3


# ghost ai modes
class GHOST_MODE:
    CHASE = 0
    SCATTER = 1


# initial position of objects
class POS:
    PACMAN = (23, 13)


# state representations
class REP:
    EMPTY = 0
    WALL = 1
    DOOR = 2
    PWRPLT = 3
    CHERRY = 4
    PACMAN = 5
    BLINKY = 6
    INKY = 7
    PINKY = 8
    CLYDE = 9

    COLOR_MAP = {
        0: "#0E0E0E",
        1: "#3A60DE",
        2: "#F255C8",
        3: "#F5DAF7",
        4: "#E3398B",
        5: "#E8D22A",
        6: "#E62C4E",
        7: "#27EBF2",
        8: "#F255C8",
        9: "#FF9F29",
    }
