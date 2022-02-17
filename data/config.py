from typing import List


class CONFIG:
    # board pattern for path and walls
    BOARD: List[List[int]] = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # board pattern for pellets and power pellets
    PELLET_BOARD: List[List[int]] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0],
        [0, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 4, 0],
        [0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0],
        [0, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 0],
        [0, 3, 0, 3, 0, 0, 0, 0, 0, 3, 0, 3, 0],
        [0, 4, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0],
        [0, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
