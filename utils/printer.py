from data.config import BOARD
from game.game import Game


def printPacmanPerfomance(ep: int, game: Game) -> None:
    consumption: int = BOARD.TOTAL_PELLET_COUNT - game.pelletProgress
    completion: float = round(consumption / BOARD.TOTAL_PELLET_COUNT * 100, 2)
    
    print(
        "ep: {}\tt: {}\tl: {}\tc: {}/68 = {}%".format(
            ep,
            game.timesteps,
            game.pelletProgress,
            consumption,
            completion,
        )
    )

    return completion
