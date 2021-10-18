from typing import Tuple

from data import DIM
from utils.coordinate import CPair


class GUIUtil:
    # calculate the pixel position of grid cell
    def calculatePos(row: int, col: int) -> Tuple[int, int, int, int]:
        x0: int = col * DIM.JUMP
        y0: int = row * DIM.JUMP
        return x0, y0, x0 + DIM.CELL, y0 + DIM.CELL

    # calculate the delta of display objects
    def calculateDxDy(curPos: CPair, prevPos: CPair) -> Tuple[int, int]:
        return (
            (curPos.col - prevPos.col) * DIM.JUMP,
            (curPos.row - prevPos.row) * DIM.JUMP,
        )
