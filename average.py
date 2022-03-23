from data.data import AGENT_CLASS_TYPE, REP
from game.game import Game, newGame
from utils.printer import printPacmanPerfomance


class App:
    def __init__(self, config: dict[str, object]) -> None:
        # agent config
        self.agents: dict[str, object] = config["agents"]

        # game config
        self.enablePwrPlt: bool = config["enablePwrPlt"]

        # neural net config files
        self.neuralnets: dict[str, str] = config["neuralnets"]

        # genomes config files
        self.genomes: dict[str, str] = config["genomes"]

        # iterations
        self.iterations: int = config["iterations"]

    def start(self) -> None:
        average: float = 0

        for i in range(self.iterations):
            average += self.runGame(i)

        print("Average Completion Rate: {}".format(average / self.iterations))

    def runGame(self, iteration: int) -> float:
        game: Game = newGame(self.agents, self.enablePwrPlt, self.neuralnets, self.genomes)

        while True:
            gameover, won, atePellet, atePwrPlt, ateGhost = game.nextStep()
            if gameover or won or game.timesteps > 200:
                break

        return printPacmanPerfomance(iteration, game, True)


if __name__ == "__main__":
    app: App = App(
        {
            "agents": {
                REP.PACMAN: AGENT_CLASS_TYPE.RAND,
                REP.BLINKY: AGENT_CLASS_TYPE.GDQL,
                "secondary": AGENT_CLASS_TYPE.RAND,
            },
            "enablePwrPlt": True,
            "genomes": {
                REP.BLINKY: ("out", "NE2303_0111", 280),
            },
            "iterations": 1000,
            "neuralnets": {
                REP.PACMAN: ("saves", "pacman", 63),
                REP.BLINKY: ("out", "RL2103_1506", 10000),
            },
        }
    )
    app.start()
